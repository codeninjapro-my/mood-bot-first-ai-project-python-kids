# Mood Bot: Build Your First AI with Python

**Teach a computer to recognise moods by learning from examples!**

In this beginner-friendly project, you'll build a tiny AI that learns word patterns from happy and sad sentences, then predicts the mood of new sentences.

🎯 **Age:** 10+  
⏱️ **Time:** 30 minutes  
💻 **Language:** Python  
🚀 **Level:** Beginner

## 🧠 What You'll Learn
- Training AI with example data
- Counting words and identifying patterns
- Using Python dictionaries, loops, and functions
- Making predictions from new sentences
- Understanding AI bias and why data matters

## 💻 Let's Build Mood Bot!

```python
# Mood Bot — Code Ninja Pro | codeninja.pro

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

word_counts = {"happy": {}, "sad": {}}

for sentence, mood in examples:
    for word in sentence.lower().split():
        word_counts[mood][word] = word_counts[mood].get(word, 0) + 1

def predict(sentence):
    scores = {"happy": 0, "sad": 0}

    for word in sentence.lower().split():
        for mood in scores:
            scores[mood] += word_counts[mood].get(word, 0)

    if scores["happy"] == scores["sad"]:
        return "not sure yet - teach me more!", scores

    return max(scores, key=scores.get), scores

while True:
    text = input("Tell me something (or 'quit'): ")

    if text == "quit":
        break

    mood, scores = predict(text)
    print(f"Mood: {mood} (scores: {scores})")
```

## 🚀 Challenges to Try
1. **Fix the bias:** Add more training examples.
2. **Teach it more:** Create 10 new sentences.
3. **Add a new mood:** Teach Mood Bot to recognise anger.
4. **Improve predictions:** Ignore common words like "the" and "was".
5. **Measure confidence:** Compare the scores for each mood.

## 💡 The Big AI Lesson

AI learns patterns from data, but it can make mistakes when its training examples are limited or biased.

Build it, test it, and improve it to discover why good data matters!

## 🌟 Learn AI with Code Ninja Pro

At **[Code Ninja Pro](https://codeninja.pro)**, kids learn coding, AI, and robotics by building real projects.

🎓 Ready for your child's AI adventure?

👉 **[Book a Free Trial Class](https://codeninja.pro/free-trial)**

⭐ Learn. Build. Innovate. 🥷
