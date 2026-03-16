def policy_decision(injection_score, pii_results):

    if injection_score > 0.3:
        return "BLOCK"

    if len(pii_results) > 0:
        return "MASK"

    return "ALLOW"