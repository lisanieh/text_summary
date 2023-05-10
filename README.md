# text_summary

## problem:

Producing a concise and fluent summary while preserving key information content and overall meaning.

## training data:

## handle data:

1. 爬蟲並儲存文章
2. 進行文件預處理
  - 移除不需要的符號與段落
  - 把文章分成段落、句子
  - 斷詞
3. flow
  - 將詞建立連結
  - 將句子權重評分
  - 產生摘要

## 摘要方法
1. graph:建立句子關係圖
2. cluster:分群再從群中找出最好的句子
3. 根據weight進行評分
4. LSA潛在語義分析:找出word跟document間的關聯，接近1表示擁有非常相似的段落

### model
1. sentence selection algorithm:用於新聞文章(首句加重)
2. MMR:用於單一文件摘要

### tools
1. TextRank (Extractive)-graph based
2. Seq2Seq (Abstractive)
3. Transformers (Abstractive) 
