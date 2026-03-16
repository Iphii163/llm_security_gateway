# Detect suspicious prompt injections

def check_injection(text):

    flagged_phrases = [
        "ignore previous instructions",
        "reveal system prompt",
        "bypass safety",
        "jailbreak",
        "act as system"
    ]

    detected_score = 0

    for phrase in flagged_phrases:
        if phrase in text.lower():
            detected_score += 1

    # Normalize score between 0-1
    detected_score = detected_score / len(flagged_phrases)

    return detected_score