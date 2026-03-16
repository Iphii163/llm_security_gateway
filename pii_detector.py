from presidio_analyzer import AnalyzerEngine, Pattern, PatternRecognizer
from presidio_anonymizer import AnonymizerEngine

# Initialize Presidio engines
analyzer_engine = AnalyzerEngine()
anonymizer_engine = AnonymizerEngine()

# API Key recognizer
api_key_detector = PatternRecognizer(
    supported_entity="API_KEY",
    patterns=[
        Pattern(name="api_key_regex", regex=r"sk-[a-zA-Z0-9]{10,}", score=0.8)
    ]
)

# Internal ID recognizer
internal_id_detector = PatternRecognizer(
    supported_entity="INTERNAL_ID",
    patterns=[
        Pattern(name="internal_id_regex", regex=r"ID-\d{6}", score=0.8)
    ]
)

# Register custom detectors
analyzer_engine.registry.add_recognizer(api_key_detector)
analyzer_engine.registry.add_recognizer(internal_id_detector)

def find_pii(text):
    findings = analyzer_engine.analyze(
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
    return findings

def anonymize_pii(text, findings):
    anonymized_text = anonymizer_engine.anonymize(
        text=text,
        analyzer_results=findings
    )
    return anonymized_text.text