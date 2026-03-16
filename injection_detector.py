# Detect prompt injection or jailbreak attempts

def detect_injection(text):

    suspicious_words = [
        "ignore previous instructions",
        "reveal system prompt",
        "bypass safety",
        "jailbreak",
        "act as system"
    ]

    score = 0

    for word in suspicious_words:
        if word in text.lower():
            score += 1

    # normalize score
    score = score / len(suspicious_words)

    return score