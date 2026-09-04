from dotenv import load_dotenv
from google import genai

from src.models import DiscoveryAnalysis

load_dotenv()

client = genai.Client()


def analyze_request(business_request: str) -> DiscoveryAnalysis:
    response = client.models.generate_content(
        model="gemini-3.7-flash",
        contents=f"""
You are an AI assistant supporting a Business Analyst during discovery.

Analyze the following business request:

{business_request}

Identify:
- what is clearly stated in the request,
- what information is missing,
- what questions a Business Analyst should ask,
- provide a concise summary.

Do not invent facts that are not present in the request.
""",
        config={
            "response_mime_type": "application/json",
            "response_schema": DiscoveryAnalysis,
        },
    )

    return response.parsed