import pandas as pd
from preprocess import preprocess

df = pd.read_csv('train.txt', sep=';', header=None, names=['text', 'emotion'])
print(df.head(10))
print(df['emotion'].value_counts())
df['word_count'] = df['text'].apply(lambda x: len(x.split()))
print(df['word_count'].mean())

samples = [
    df[df['emotion'] == 'joy']['text'].iloc[0],
    df[df['emotion'] == 'sadness']['text'].iloc[0],
    df[df['emotion'] == 'anger']['text'].iloc[0]
]

for s in samples:
    print(f"Original: {s}")
    print(f"Tokens: {preprocess(s)}")
    print("---")