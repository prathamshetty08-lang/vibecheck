import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word, pos='v') for word in tokens]
    return tokens

# Test on 5 sentences
if __name__ == "__main__":
    # all your test code here
 sentences = [
    "I'm SO hyped!!!!",
    "ugh... everything's going wrong",
    "I feel really happy and excited today",
    "I am so stressed and anxious right now",
    "Everything feels calm and peaceful"
 ]

for s in sentences:
     print(f"Original: {s}")
     print(f"Tokens: {preprocess(s)}")
     print("---")