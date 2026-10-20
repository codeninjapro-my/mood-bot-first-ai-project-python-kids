# Mood Bot: a tiny AI that learns from examples
# Code Ninja Pro — codeninja.pro

# 1. Training data: examples the "machine" learns from
examples = [
    ("I love this game", "happy"),
    ("today was awesome", "happy"),
    ("my friends are so fun", "happy"),
    ("I got full marks", "happy"),
    ("I hate homework", "sad"),
    ("today was boring", "sad"),
    ("I lost my favourite pen", "sad"),
    ("my team lost the match", "sad"),
]

# 2. Training: count how often each word appears in each mood
word_counts = {"happy": {}, "sad": {}}
for sentence, mood in examples:
    for word in sentence.lower().split():
        word_counts[mood][word] = word_counts[mood].get(word, 0) + 1

# 3. Predicting: score a new sentence against each mood
def predict(sentence):
    scores = {"happy": 0, "sad": 0}
    for word in sentence.lower().split():
        for mood in scores:
            scores[mood] += word_counts[mood].get(word, 0)
    if scores["happy"] == scores["sad"]:
        return "not sure yet - teach me more!", scores
    return max(scores, key=scores.get), scores

# 4. Try it!
while True:
    text = input("Tell me something (or 'quit'): ")
    if text == "quit":
        break
    mood, scores = predict(text)
    print(f"Mood: {mood}  (scores: {scores})")
