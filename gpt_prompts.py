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
    You are an expert in Nigerian agriculture, processing, and market advisory.
    The user has entered: '{crop_name}'
    Your first task is to verify whether this input is a real farm produce — such as a crop, livestock, or commonly cultivated agricultural product in Nigeria.
    - If the input is NOT a valid farm produce, politely respond with:
    ❌ 'This does not seem to be a valid farm produce or crop. Please enter something like cassava, maize, plantain, or tomatoes.'
    - If it is valid, provide detailed guidance with the following sections:
    1. ✅ Best time to **plant** {crop_name} in Nigeria (based on weather/seasons)
    2. ✅ Best time to **harvest** {crop_name}
    3. ✅ Best time to **sell** {crop_name} for market value
    4. ✅ Best region/state to grow {crop_name} in Nigeria
    5. 🏭 How to process {crop_name} into value-added products
    6. 🧊 Storage tips — both short-term and long-term
    7. 📦 Packaging advice to improve shelf-life and appeal
    8. 📍 Suggested platforms or market locations to sell
    9. 💡 A catchy Nigerian business name suggestion related to {crop_name}
    Respond clearly and in bullet points only.
"""


    response = client.chat.completions.create(
        model="farmgpt",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content
