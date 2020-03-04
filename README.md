# nlp-emotion-analysis-core
Core NLP library for extracting and analysing emotion and group dynamics in a group setting.

## Key functionalities

### 1. Emotion extraction
Emotion extraction is based the eight basic emotions model proposed by Plutchik[1]. The extraction is based on a vocabulary 
curated using wordembedding models. Online conversations related to health were used to train the word embedding model which capture the 
contextual relationships among terms. The trained model is then used to query for similar terms. Scripts to train the word embedding model,
query for similar terms and visualizations are included in core/emotions/ folder.
Emotion extraction is enriched with handling negation, intensifiers and is able to calculate the intensity of each emotion.


### 2. User enagagement measures
User engagement in a group is measured based on two main components:
  i. Emotion enagagement
  ii. Participation based on number of posts etc.
  

### 3. Clinical information extraction
Clinical information can be extracted using a curated vocabulary of clinical terms. Physcial symptom extractor is added as a demonstration.


### 4. Keyphrase extraction
Keyphrase extraction is based on RAKE [2], which automatically extracts significant phrases from text.





Examples for emotion extraction, physical symptoms extraction and keyphrase extraction are included in the main.py







#### References:

[1] Plutchik, R. (1984). Emotions: A general psychoevolutionary theory. Approaches to emotion, 1984, 197-219.

[2] Rose, S., Engel, D., Cramer, N., & Cowley, W. (2010). Automatic keyword extraction from individual documents. Text mining: applications and theory, 1, 1-20.
