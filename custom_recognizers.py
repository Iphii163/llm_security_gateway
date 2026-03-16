from presidio_analyzer import PatternRecognizer

# Custom API key recognizer
api_key_recognizer = PatternRecognizer(
    supported_entity="API_KEY",
    patterns=[
        {
            "name": "api_key_pattern",
            "regex": "sk-[a-zA-Z0-9]{10,}",
            "score": 0.8
        }
    ]
)

# Custom Internal ID recognizer
internal_id_recognizer = PatternRecognizer(
    supported_entity="INTERNAL_ID",
    patterns=[
        {
            "name": "internal_id_pattern",
            "regex": "INT-[0-9]{4,}",
            "score": 0.8
        }
    ]
)

# Custom phone recognizer
phone_recognizer = PatternRecognizer(
    supported_entity="CUSTOM_PHONE",
    patterns=[
        {
            "name": "phone_pattern",
            "regex": "03[0-9]{9}",
            "score": 0.8
        }
    ]
)