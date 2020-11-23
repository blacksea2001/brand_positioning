# 視覺化口碑雷達圖

企業的品牌以及形象，是企業一向非常重要的無形資產，沒有一個企業會忽視他的重要性，尤其會與其競爭者相互比較，知道自己在市場上的位置。比起傳統的行銷研究工具，我們應用了行銷資料科學工具，利用網路爬文，將消費者在網路上談論公司產品（品牌）、競爭者產品（品牌）的文章進行擷取，透過語言模型(本專案使用GloVe)對這些文章進行分析，了解該目標市場討論的屬性為何？重視的屬性為何？並且在這些屬性上，顧客對各競爭者屬性的知覺狀況。


## Data

此處使用洗錢新聞作為範例，共341篇。欲使用自己的文本，請放入 /data 資料夾中。


## 訓練文字向量

先執行 preprocess.py 得到 train.txt

    $ cd model
    $ python proprecess.py

再將 train.txt 放到 GloVe 專案中，執行以下步驟

    $ cd glove && make
    $ ./demo.sh

得到詞向量文件 vectors.txt
並將 GloVe 訓練時 vocab size 及 vector size 資訊加到 vectors.txt 第一行

![image](/data/pic/glove_training.png)


## 產生雷達圖

執行 radar.py 可得雷達圖。
