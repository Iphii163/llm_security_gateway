def evaluate_policy(injection_score, pii_findings):

    if injection_score > 0.3:
        return "BLOCKED"

    if len(pii_findings) > 0:
        return "MASKED"

    return "ALLOWED"