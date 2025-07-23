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

    🔍 First: Check if this is a valid farm produce commonly found in Nigeria.

    You MUST consider it valid if it's in this list of Nigerian farm products (crops, fruits, vegetables, etc.):

    - **Cereals/Grains**: maize, rice, millet, sorghum, guinea corn
    - **Tubers**: yam, cassava, potato, sweet potato
    - **Legumes**: beans, soybeans, groundnut, bambara nut
    - **Vegetables**: okra, ugu (fluted pumpkin), bitter leaf, waterleaf, spinach, ewedu, garden egg
    - **Fruits**: mango, orange, cashew, guava, pineapple, banana, plantain, pawpaw, watermelon, coconut
    - **Spices/Roots**: ginger, garlic, turmeric
    - **Oil-producing**: oil palm, groundnut, coconut
    - **Others**: cocoa, kolanut, sugarcane, sesame, cotton, egusi (melon), tigernut

    ❌ If it is clearly **NOT** a farm produce (e.g. phone, laptop, aeroplane), respond with:
    "❌ '{crop_name}' is not a recognized farm produce. Please enter something like cassava, maize, tomatoes, catfish, or oranges."

    ✅ If it is valid, provide the following response:

    - Format your response using *numbered bullet points (1 to 9)* and make it bold
    - Bold the section titles (e.g. 1. Best time to plant...)
    - DO NOT bold the explanations
    - Keep it clear, practical, and helpful for Nigerian farmers
    

    1. Best time to plant {crop_name} according to Nigeria weather
    2. Best time to harvest {crop_name} according to Nigeria weather
    3. Best time to sell {crop_name} according to Nigeria weather
    4. Best region to plant {crop_name} in Nigeria
    5. How to process it into value-added products
    6. Storage tips (short-term and long-term)
    7. Packaging advice
    8. Suggested platforms or locations to sell
    9. A catchy Nigerian business name for the product
    """

    response = client.chat.completions.create(
        model="farmgpt",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    # return response.choices[0].message.content
    raw = response.choices[0].message.content
    cleaned = "\n".join([line.strip() for line in raw.split('\n') if line.strip()])
    return cleaned
