# nlp-emotion-analysis-core
Core NLP library for extracting and analysing emotion and group dynamics in a group setting.

## Key functionalities

### 1. Emotion extraction
Emotion extraction is based the eight basic emotions model proposed by Plutchik[1]. The extraction is based on a vocabulary 
curated using wordembedding models. Online conversations related to health were used to train the word embedding model which capture the 
contextual relationships among terms. The trained model is then used to query for similar terms. Scripts to train the word embedding model,
query for similar terms and visualizations are included in core/emotions/ folder.
Emotion extraction is enriched with handling negation, intensifiers and is able to calculate the intensity of each emotion.

<img src="https://www.researchgate.net/profile/Gerardo_Maupome/publication/258313558/figure/fig1/AS:297350959517696@1447905401049/Plutchiks-wheel-of-emotions-with-basic-emotions-and-derivative-emotions-and-cone-like.png" data-canonical-src="https://www.researchgate.net/profile/Gerardo_Maupome/publication/258313558/figure/fig1/AS:297350959517696@1447905401049/Plutchiks-wheel-of-emotions-with-basic-emotions-and-derivative-emotions-and-cone-like.png" width="300" height="300" />
<h6>Image retrieved from [2].<h6>


### 2. User enagagement measures
User engagement in a group is measured based on two main components:
  i. Emotion enagagement
  ii. Participation based on number of posts etc.
  

### 3. Clinical information extraction
Clinical information can be extracted using a curated vocabulary of clinical terms. Physcial symptom extractor is added as a demonstration.


### 4. Keyphrase extraction
Keyphrase extraction is based on RAKE [3], which automatically extracts significant phrases from text.





Examples for emotion extraction, physical symptoms extraction and keyphrase extraction are included in the main.py







#### References:

[1] Plutchik, R. (1984). Emotions: A general psychoevolutionary theory. Approaches to emotion, 1984, 197-219.

[2] Retrieved from: https://www.researchgate.net/profile/Gerardo_Maupome/publication/258313558/figure/fig1/AS:297350959517696@1447905401049/Plutchiks-wheel-of-emotions-with-basic-emotions-and-derivative-emotions-and-cone-like.png

[3] Rose, S., Engel, D., Cramer, N., & Cowley, W. (2010). Automatic keyword extraction from individual documents. Text mining: applications and theory, 1, 1-20.
