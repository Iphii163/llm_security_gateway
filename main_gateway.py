import time

from injection_detector import detect_injection
from pii_detector import detect_pii, mask_pii
from policy_engine import policy_decision


def process_input(user_input):

    start = time.time()

    # Injection detection
    injection_score = detect_injection(user_input)

    # PII detection
    pii_results = detect_pii(user_input)

    # policy decision
    decision = policy_decision(injection_score, pii_results)

    if decision == "BLOCK":
        output = "Request Blocked (Prompt Injection Detected)"

    elif decision == "MASK":
        output = mask_pii(user_input, pii_results)

    else:
        output = user_input

    latency = time.time() - start

    print("\n----- Result -----")
    print("Injection Score:", injection_score)
    print("Decision:", decision)
    print("Output:", output)
    print("Latency:", latency)


if __name__ == "__main__":

    user_input = input("Enter prompt: ")
    process_input(user_input)