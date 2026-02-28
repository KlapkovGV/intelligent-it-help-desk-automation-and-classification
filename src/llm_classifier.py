import os
from google import genai
from src.config import CATEGORIES, MODEL_NAME

def get_llm_classification(description, api_key):
    client = genai.Client(api_key=api_key)
    
    prompt = f"""
  You are an IT help desk ticket classifier. Your job is to categorize the following ticket into ONE of these categories:
  - Network.
  - Software.
  - Account.
  - Training.
  - Security.
  - Licensing.
  - Communication.
  - RemoteWork.
  - Hardware.
  - Infrastructure.
  - Performance.

  Classification Logic (CRITICAL):
  - Training: User doesn't know HOW to use something. Requests for "guidance", "resources", "how-to", "navigation help", or "manuals".
  - Software: Technical bugs, "crashes", "conflicts", "log analysis for errors", "installation", or "configuration" of apps.
  - Security: Data breaches, "malware", "phishing", "unauthorized access", "firewall rules", or "antivirus alerts".

  CRITICAL RULES (FOLLOW THESE FIRST):
  1. If the user mentions "guidance" or "resources" regarding a system (even if it's Software or Network), you MUST classify it as 'Training'.
  2. If the user mentions "crashes", "software conflict", or "analyzing logs" to fix a bug, you MUST classify it as 'Software'.
  3. Use 'Security' ONLY for actual threats or access violations. A software crash is NEVER a security issue.
  4. Do NOT classify as 'Communication' just because it's an email/polite message. Only use it for communication software issues.
  5. Ignore greetings ("Hello"), signatures ("Thanks, Alex"), and emojis. Focus only on the core request.

  Ticket description: {description}

  Return ONLY the category name without any additional text.
  """
    
    try:
        response = client.models.generate_content(model=MODEL_NAME, contents=prompt)
        result = response.text.strip().replace("*", "").replace("\"", "").replace("'", "").strip()
        
        # Твоя логика проверки результата
        for k in CATEGORIES:
            if k.lower() in result.lower():
                return k
        return "Ambiguous"
    except Exception as e:
        return f"Error: {e}"
