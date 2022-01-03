from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer

corpus_clean = [
   "j'adore vraiment cette ville",
   "je suis super triste en ce moment",
   "je ne sais pas quoi penser de la situation",
   "comment je déteste les radins, ca me dégoute",
   "tu me rends vraiment heureuse",
   "tu me rends heureuse",
   "tu me rends super heureuse",
   "tu me rends extrêmeent heureuse"
]
polarity = []
for tweet in corpus_clean:
   polarity.append(TextBlob(tweet, pos_tagger=PatternTagger(), analyzer=PatternAnalyzer()).sentiment[0])


if len(corpus_clean)==len(polarity):
   for sentence, pol in zip(corpus_clean, polarity):
      print(str(sentence)+": "+str(pol))
