# Examining Translationese Using Embeddings 
This project makes use of the [Europarl Corpus](https://aclanthology.org/2005.mtsummit-papers.11/), specifically prepared in parallel for [French and English](https://arxiv.org/abs/1509.03611). It produces embeddings for both translated and untranslated portions of the corpus, and compares them to see if embeddings can identifying markers of translationese. These embeddings are done for both English and French. The data as it has been processed for these purposes has been excluded, however the file to process it is available so this can be reproduced by using Rabinovich et. al's publicly available data. 

# Sources
Heavily based on lecture and lab content by [Dr. Jonathan Dunn](https://www.jdunn.name/). 
Additional sources include: 
- https://www.geeksforgeeks.org/continuous-bag-of-words-cbow-in-nlp/  
- https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html 
