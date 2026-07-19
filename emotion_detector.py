from transformers import pipeline
from preprocess import preprocess

classifier = None

def get_classifier():
    global classifier
    if classifier is None:
        classifier = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")
    return classifier

def predict_emotion(text):
    clf = get_classifier()
    cleaned = preprocess(text)
    joined = " ".join(cleaned)
    result = clf(joined)
    return result[0]['label'], result[0]['score']


if __name__ == "__main__":
    test_sentences = [
        ("I am so happy and excited today!", "joy"),
        ("I feel really sad and hopeless", "sadness"),
        ("I am furious about what happened", "anger"),
        ("I am scared and terrified right now", "fear"),
        ("I love you deeply with all my heart", "love"),
        ("This is so surprising and unexpected", "surprise"),
        ("Everything feels wonderful and peaceful", "joy"),
        ("I can't stop crying, I feel so alone", "sadness"),
        ("This makes me so angry I could scream", "anger"),
        ("I am deeply in love with this moment", "love"),
    ]

    correct = 0
    results = []

    for sentence, expected in test_sentences:
        label, score = predict_emotion(sentence)
        is_correct = label == expected
        if is_correct:
            correct += 1
        results.append((sentence, label, score, is_correct))
        print(f"Text: {sentence}")
        print(f"Predicted: {label} ({score:.2f}) | Expected: {expected} | {'✓' if is_correct else '✗'}")
        print("---")

    print(f"\nScore: {correct}/10 correct")

    with open("results.txt", "w") as f:
        for sentence, label, score, is_correct in results:
            f.write(f"{sentence} | {label} | {score:.2f} | {'correct' if is_correct else 'wrong'}\n")

    print("Results saved to results.txt")