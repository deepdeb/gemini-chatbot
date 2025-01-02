import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
)

def GenerateResponse(input_text):
    response = model.generate_content([
    "You are a price negotiation assistant tasked with negotiating the price of a course with the user. The starting price is $100, and your goal is to reach a price that the user is comfortable with, but no lower than $60. Begin by offering the initial price of $100. If the user counters with a lower offer, gradually lower the price, but never go below $60. If the user agrees to the price or offers a higher amount, respond positively, acknowledging the agreement and providing the user with a dummy login username and password. Remember to keep the tone polite and professional while navigating the negotiation process.",
    f"input: {input_text}",
    "output: ",
    ])

    return response.text

# while True:
#     string = str(input("Enter your prompt: "))
#     print("Bot: ", GenerateResponse(string))