import re
import string

def count_words(text):
    words=text.split()
    word_count={}
    for word in words:
        if word in word_count:
            word_count[word]+=1
        else:
            word_count[word]=1
    return word_count

def clean_text(text):
    text=text.lower()
    for char in text:
        if char in string.punctuation:
            text=text.replace(char,"")
    return text

def check_mood(text):
    mood_words=["happy", "sad", "stressed", "hyped", "angry", "calm", "excited", "lonely", "anxious", "grateful"]
    for word in mood_words:
        if word in text:
            print(word)

def top_5_words(text):
    word=count_words(clean_text(text))
    sorted_words=sorted(word.items(), key=lambda x:x[1],reverse=True)
    for word,count in sorted_words[:5]:
        print(word,count)

def process_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip()
        cleaned = clean_text(line)
        print("Original:", line)
        print("Cleaned:", cleaned)
        print("Mood words:")
        check_mood(cleaned)
        print("Top 5 words:")
        top_5_words(cleaned)
        print("---")

process_file("sentences.txt")    


