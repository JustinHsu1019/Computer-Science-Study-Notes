import io
import zipfile
from langchain.schema import HumanMessage
from langchain.chat_models import AzureChatOpenAI
import configparser
import logging.config
from openai.error import RateLimitError

LOGGING_CONFIG = 'logging.ini'
logging.config.fileConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)

def load_config():
    config = configparser.ConfigParser()
    config.read('const.ini')
    return config['OpenAI']

config = load_config()

def do_openai(messages, retry_count=3):
    if retry_count <= 0:
        logger.error("Max retry attempts reached. Exiting.")
        print("Max retry attempts reached. Exiting.")
        return "系統發生錯誤，請通知系統管理員!"

    openAI = AzureChatOpenAI(
        openai_api_base=config['openai_api_base'],
        openai_api_version=config['openai_api_version'],
        deployment_name=config['completions_model'],
        openai_api_key=config['openai_azure_api_key'],
        openai_api_type=config['openai_api_type'],
        temperature=0,
        max_tokens=16000
    )
    try:
        res = openAI(messages)
        return res.content
    except RateLimitError:
        logger.warning("get rate limit, run again")
        print("get rate limit, run again")
        return do_openai(messages, retry_count-1)
    except Exception as e:
        logger.error(f"get error: {e}")
        print(f"get error: {e}")
        return "系統發生錯誤，請通知系統管理員!"

def notesprocess(zip_stream):
    output_zip_stream = io.BytesIO()

    with zipfile.ZipFile(zip_stream) as input_zip, zipfile.ZipFile(output_zip_stream, 'w') as output_zip:
        for file_info in input_zip.infolist():
            if file_info.filename.endswith('.txt'):
                with input_zip.open(file_info) as file:
                    content = file.read().decode('utf-8')
                    prompt = f"""
請根據下面的文本內容摘錄出重要的幾個知識點。對於每個知識點，請提供一個清晰的大標題，並給出以下信息：

1. 該知識點的簡介
2. 該知識點重要的三個細節
3. 關於該知識點可能考的三個考題及詳解

請確保所有輸出內容嚴格依照所提供文本的知識，並用繁體中文書寫（專有名詞保持英文原樣）。以下是所需摘錄的文本內容：

{content}

根據上述文本內容，請開始摘錄並組織知識點。
"""
                    messages = [HumanMessage(content=prompt)]
                    summary = do_openai(messages)
                    if "系統發生錯誤" in summary:
                        logger.error("Error in summarizing the content")
                        return None
                    output_zip.writestr(file_info.filename, summary)
    output_zip_stream.seek(0)

    return output_zip_stream

if __name__ == "__main__":
    pass
