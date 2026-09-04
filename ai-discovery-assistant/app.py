from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel

load_dotenv()

client = genai.Client()


class DiscoveryAnalysis(BaseModel):
    clear: list[str]
    missing_information: list[str]
    discovery_questions: list[str]
    summary: str

business_request = """
We need to improve visibility of inventory across our warehouses.
Currently, each warehouse uses different spreadsheets and reporting methods.
Management wants one consistent view of stock levels and inventory movements.
"""
response = client.models.generate_content(
    model="gemini-3.7-flash",
    contents=f"""
Analyze this business request:

{business_request}

Identify what is clear, what information is missing,
and what questions a Business Analyst should ask during the discovery meeting.
""",
    config={
        "response_mime_type": "application/json",
        "response_schema": DiscoveryAnalysis,
    },
)

analysis = response.parsed

print("CLEAR:")
print(analysis.clear)

print("\nMISSING INFORMATION:")
print(analysis.missing_information)

print("\nDISCOVERY QUESTIONS:")
print(analysis.discovery_questions)

print("\nSUMMARY:")
print(analysis.summary)