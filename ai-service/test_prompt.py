import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.groq_client import GroqClient
from dotenv import load_dotenv

load_dotenv()

client = GroqClient()

test_inputs = [
    {
        "asset_name": "Web Server",
        "asset_type": "Server",
        "description": "Public facing web server with no firewall"
    },
    {
        "asset_name": "Customer Database",
        "asset_type": "Database",
        "description": "PostgreSQL database storing customer PII data"
    },
    {
        "asset_name": "Employee Laptops",
        "asset_type": "Endpoint",
        "description": "Windows laptops with no antivirus installed"
    },
    {
        "asset_name": "Payment Gateway",
        "asset_type": "Application",
        "description": "Handles credit card transactions, outdated SSL"
    },
    {
        "asset_name": "Internal WiFi Network",
        "asset_type": "Network",
        "description": "Office WiFi with WEP encryption"
    }
]

with open("prompts/describe_prompt.txt", "r") as f:
    prompt_template = f.read()

print("Testing 5 inputs...\n")

for i, input_data in enumerate(test_inputs, 1):
    print(f"Test {i}: {input_data['asset_name']}")
    
    prompt = prompt_template.format(**input_data)
    
    messages = [{"role": "user", "content": prompt}]
    result = client.call(messages)
    
    if result:
        print(f"✅ Response received")
        print(result)
    else:
        print(f"❌ Failed")
    print("-" * 50)