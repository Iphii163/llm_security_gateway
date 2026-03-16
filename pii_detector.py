from presidio_analyzer import AnalyzerEngine, Pattern, PatternRecognizer
from presidio_anonymizer import AnonymizerEngine

# Initialize Presidio engines
analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()

# Custom recognizer for API_KEY                         
api_key_recognizer = PatternRecognizer(
    supported_entity="API_KEY",
    patterns=[
        Pattern(name="api_key_pattern", regex=r"sk-[a-zA-Z0-9]{10,}", score=0.8)
    ]
)

# Custom recognizer for INTERNAL_ID
internal_id_recognizer = PatternRecognizer(
    supported_entity="INTERNAL_ID",
    patterns=[
        Pattern(name="internal_id_pattern", regex=r"ID-\d{6}", score=0.8)
    ]
)

# Add custom recognizers to the analyzer
analyzer.registry.add_recognizer(api_key_recognizer)
analyzer.registry.add_recognizer(internal_id_recognizer)


def detect_pii(text):
    results = analyzer.analyze(
        text=text,
        entities=[
            "PHONE_NUMBER",
            "EMAIL_ADDRESS",
            "CREDIT_CARD",
            "API_KEY",
            "INTERNAL_ID"
        ],
        language="en"
    )
    return results


def mask_pii(text, results):
    anonymized = anonymizer.anonymize(
        text=text,
        analyzer_results=results
    )
    return anonymized.text


