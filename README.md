llm-security-gateway/
│
├── gateway/             # Core modules
├── configs/             # Threshold configurations
├── evaluation/          # Test cases
├── run_demo.py          # Demo script
├── requirements.txt
└── README.md

Installation:

1. Clone the repository:
 git clone <repo_url>
 cd llm-security-gateway

2. Install dependencies:
 pip install -r requirements.txt

Usage
Run the demo script:
 python run_demo.py

Enter your input text, and the gateway will return:
Decision: BLOCK / MASK / ALLOW
Processed output
Latency