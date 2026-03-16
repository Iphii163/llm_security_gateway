import time
from injection_detector import check_injection
from pii_detector import find_pii, anonymize_pii
from policy_engine import evaluate_policy

def handle_input(user_text):

    start_time = time.time()

    # Step 1: Check for injection
    injection_level = check_injection(user_text)

    # Step 2: Detect PII
    pii_items = find_pii(user_text)

    # Step 3: Policy evaluation
    action = evaluate_policy(injection_level, pii_items)

    if action == "BLOCKED":
        output = "Request Denied (Injection Detected)"
    elif action == "MASKED":
        output = anonymize_pii(user_text, pii_items)
    else:
        output = user_text

    elapsed_time = time.time() - start_time

    print("\n--- Analysis Result ---")
    print("Injection Level:", injection_level)
    print("Policy Decision:", action)
    print("Processed Output:", output)
    print("Processing Time:", elapsed_time)

if __name__ == "__main__":
    user_text = input("Enter your prompt: ")
    handle_input(user_text)