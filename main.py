import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as pyplot
import time
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn .model_selection import train_test_split
from sklearn.metrics import classification_report 
from sklearn.metrics import confusion_matrix
from nltk.tokenize import RegexpTokenizer
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from bs4 import BeautifulSoup
from PIL import Image
import pickle 
import warnings
warnings.filterwarnings('ignore')
df= pd.read_csv("phishing_site_urls.csv")
df.head()
sns.countplot(x="Label",data=df)
tokenizer = RegexpTokenizer(r'[A-Za-z]+')
tokenizer.tokenize(df.URL[0]) 
stemmer = SnowballStemmer("english")
bad_sites = df[df.Label == 'bad']
good_sites = df[df.Label == 'good']
bad_sites.head()
good_sites.head()
df.head()
for (Label), group in df.groupby(['Label']):
     group.to_csv(f'urls/{Label}.csv', index=False)