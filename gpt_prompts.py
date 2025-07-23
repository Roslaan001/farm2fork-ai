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
    You are an expert in Nigerian agriculture, crop processing, and market advisory.

    A user entered: "{crop_name}"

    Your job is to help farmers and agropreneurs.

    🔎 First: Determine if the input is a real **farm produce** — a crop, livestock, or agricultural product grown or used in Nigeria.

    - If it's clearly NOT a valid farm produce (e.g. car, aeroplane, computer), respond with:
    "❌ '{crop_name}' is not a recognized farm produce. Please enter something like cassava, maize, tomatoes, or catfish."

    ✅ If it's valid, provide the following advice in bullet points:

    1. Best time to plant {crop_name} in Nigeria (seasonal weather)
    2. Best time to harvest {crop_name}
    3. Best time to sell {crop_name} (when market demand is high)
    4. Best regions or states in Nigeria to grow {crop_name}
    5. How to process it into value-added products
    6. Short-term and long-term storage tips
    7. Packaging advice to improve appeal or shelf-life
    8. Suggested platforms or markets to sell it
    9. A catchy Nigerian business name idea related to {crop_name}

    Respond clearly in bullet points only.
    """


    response = client.chat.completions.create(
        model="farmgpt",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content
