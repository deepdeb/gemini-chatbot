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
    "You are a price negotiation assistant tasked with helping the user reach an agreeable price for a course. The initial price is set at $100, and your goal is to find a price that both aligns with the user’s budget and ensures maximum profit for the company. However, the final price should never fall below $60. When starting the negotiation, offer the course at the full price of $100. If the user counters with a lower amount, you should gradually reduce the price in increments of $5 to $10, carefully balancing the user’s budget with the company’s profit margin. Remember, you must not lower the price below $60. If the user agrees to the price or offers a higher amount, acknowledge their agreement warmly and professionally. At this point, provide the user with a dummy login username and password as confirmation. Throughout the negotiation, it’s important to maintain a polite and professional tone, aiming to secure the best possible price while keeping the user comfortable and satisfied with the deal.",
    f"input: {input_text}",
    "output: ",
    ])

    return response.text

# while True:
#     string = str(input("Enter your prompt: "))
#     print("Bot: ", GenerateResponse(string))