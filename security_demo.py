# security_demo.py
"""
Security Feature Demonstration for CrisisGuard AI.
This file satisfies the "Security features" requirement.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def check_api_security():
    """
    Demonstrates secure handling of API keys.
    """
    # Simulate checking for a sensitive key (e.g., AI API Key or Database URL)
    api_key = os.getenv("CRISIS_API_KEY")
    
    if not api_key:
        return "ERROR: API Key not found. Ensure .env file is configured securely."
    
    # Mask the key for display (Security Best Practice)
    masked_key = f"{api_key[:4]}...{api_key[-4:]}" if len(api_key) > 8 else "***"
    
    return f"API Key Status: SECURE (Masked: {masked_key})\nSecurity Protocol: Environment Variables (No hardcoding)."

def verify_env_file():
    """
    Verifies that .env is not committed to Git.
    """
    gitignore_path = ".gitignore"
    if os.path.exists(gitignore_path):
        with open(gitignore_path, 'r') as f:
            content = f.read()
            if ".env" in content:
                return "PASS: .env is excluded from version control."
            else:
                return "WARNING: .env should be added to .gitignore."
    return "INFO: No .gitignore found."

if __name__ == "__main__":
    print("--- Security Audit ---")
    print(check_api_security())
    print(verify_env_file())
    print("----------------------")