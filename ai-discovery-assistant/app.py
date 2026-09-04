from dotenv import load_dotenv
load_dotenv()

from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.7-flash",
    contents="""
You are an AI assistant supporting a Business Analyst during discovery.

Analyze the following business request:

"We need to improve visibility of inventory across our warehouses.
Currently, each warehouse uses different spreadsheets and reporting methods.
Management wants one consistent view of stock levels and inventory movements."

Identify:
1. What is clear from the request.
2. What information is missing.
3. What questions a Business Analyst should ask during the discovery meeting.
"""
)

print(response.text)