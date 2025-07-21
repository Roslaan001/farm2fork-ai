from openai import AzureOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"),
api_version = "2024-10-21",
api_key = os.getenv("AZURE_OPENAI_KEY")
)

def get_farm2fork_advice(crop_name):
    prompt = f"""
You are an expert in agricultural processing and market advisory in Nigeria.

A farmer has harvested '{crop_name}' and wants advice.

Please provide:
1. Best time to plant {crop_name} according to Nigeria weather
2. Best time to harvest {crop_name} according to Nigeria weather
3. Best time to sell {crop_name} according to Nigeria weather
4. Best region to plant {crop_name} according to Nigeria weather
5. How to process it into value-added products.
6. Storage tips (short-term and long-term).
7. Packaging advice.
8. Suggested platforms or locations to sell.
9. A catchy Nigerian business name for the product.

Respond clearly in bullet points.
"""

    response = client.chat.completions.create(
        model="farmgpt",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content
