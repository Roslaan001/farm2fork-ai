import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_type = "azure"
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_version = "2023-12-01-preview"
openai.api_key = os.getenv("AZURE_OPENAI_KEY")

def get_farm2fork_advice(crop_name):
    prompt = f"""
You are an expert in agricultural processing and market advisory in Nigeria.

A farmer has harvested '{crop_name}' and wants advice.

Please provide:
1. How to process it into value-added products.
2. Storage tips (short-term and long-term).
3. Packaging advice.
4. Suggested platforms or locations to sell.
5. A catchy Nigerian business name for the product.

Respond clearly in bullet points.
"""

    response = openai.ChatCompletion.create(
        engine="farmgpt",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response['choices'][0]['message']['content']
