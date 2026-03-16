from presidio_analyzer import PatternRecognizer

# API Key pattern recognizer
api_key_detector = PatternRecognizer(
    supported_entity="API_KEY",
    patterns=[
        {
            "name": "api_key_regex",
            "regex": "sk-[a-zA-Z0-9]{10,}",
            "score": 0.8
        }
    ]
)

# Internal ID pattern recognizer
internal_id_detector = PatternRecognizer(
    supported_entity="INTERNAL_ID",
    patterns=[
        {
            "name": "internal_id_regex",
            "regex": "INT-[0-9]{4,}",
            "score": 0.8
        }
    ]
)

# Custom phone number recognizer
phone_detector = PatternRecognizer(
    supported_entity="CUSTOM_PHONE",
    patterns=[
        {
            "name": "phone_regex",
            "regex": "03[0-9]{9}",
            "score": 0.8
        }
    ]
)