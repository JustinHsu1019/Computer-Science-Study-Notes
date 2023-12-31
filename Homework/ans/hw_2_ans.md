#### 1. [P5-1] 答案
一台電腦有 64 MB 的記憶體，每個字(word)是 4 bytes。要計算記憶體中每個字所需的位址位元(bits)如下：

- 首先計算總共有多少字：64 MB * (1024 KB / 1 MB) * (1024 bytes / 1 KB) / 4 bytes/word = 16,777,216 words
- 然後計算位址位元數：log2(16,777,216) = 24 bits

因此，需要 24 位元來位址每個字。

#### 2. [P5-3] 答案
一台假想的電腦有 16 個數據暫存器(R0 到 R15)和 1024 個記憶體字，以及 16 種不同的指令。如果一個典型的 add 指令格式為 `add M R2`，那麼一個 add 指令的最小大小是多少位元：

- 暫存器部分最少需要位元數：log2(16) = 4 bits（因為有 16 個暫存器）
- 記憶體地址部分最少需要位元數：log2(1024) = 10 bits（因為有 1024 個記憶體位置）
- 指令碼部分（為了區分不同的指令，如加法、減法等）：log2(16) = 4 bits

所以一個 add 指令至少需要 4 (指令碼) + 4 (暫存器) + 10 (記憶體地址) = 18 bits。

#### 3. [P5-5] 答案
指令寄存器的大小至少要能夠容納一個完整的指令。根據 P5-3 的計算，add 指令是 18 位元，假設所有指令的大小相同，那麼指令寄存器的大小也應該是 18 位元。

#### 4. [P5-6] 答案
程式計數器必須能夠表示記憶體中所有可能的位址。由於有 1024 個記憶體位置：

- 程式計數器所需的位元數：log2(1024) = 10 bits

#### 5. [P5-11] 答案
地址總線有 10 位元，總共可以表示 2^10 = 1024 個不同的地址。由於已經有 1000 個字用於記憶體，剩餘的地址數為：

- 可用於 I/O 的地址數：1024 - 1000 = 24

每個四暫存器控制器需要 4 個地址，因此計算機可以訪問的控制器數量為：

- 四暫存器控制器的數量：24 / 4 = 6

所以，計算機可以訪問 6 個四暫存器控制器。

#### 6. [P5-12] 答案

#### 7. [P5-13] 答案

#### 8. [P5-15] 答案
