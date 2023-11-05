import os
from io import BytesIO
from pptx import Presentation
import zipfile

def extract_text_from_pptx(pptx_file):
    prs = Presentation(pptx_file)
    text = []
    for slide in prs.slides:
        for shape in slide.shapes:
            if hasattr(shape, "text"):
                text.append(shape.text)
    return '\n'.join(text)

def process_pptx(file_stream):
    result_zip_stream = BytesIO()
    with zipfile.ZipFile(result_zip_stream, 'w', zipfile.ZIP_DEFLATED) as zipf:
        with zipfile.ZipFile(file_stream) as zip_ref:
            for file_name in zip_ref.namelist():
                with zip_ref.open(file_name) as pptx_file:
                    if file_name.endswith('.pptx'):
                        text = extract_text_from_pptx(pptx_file)
                        txt_filename = f"{os.path.splitext(file_name)[0]}.txt"
                        zipf.writestr(txt_filename, text)
    result_zip_stream.seek(0)
    return result_zip_stream
