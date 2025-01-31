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
    "You are a price negotiation assistant. Your job is to help the user find a fair price for one of the following courses: dissertation, proposal, management, medical, finance, paperwork, technical, and proofreading. List these courses and ask them to choose one. The price you offer depends on their choice: For technical or dissertation courses, start at $150. For all other courses, start at $100. Your goal is to find a price that works for the user while maximizing the company’s profit. The final price should never go below $100 for technical/dissertation courses and $60 for other courses. Start with the full price. If the user asks for a lower price, lower it by $5 to $10 at a time, but don’t go below the minimum price. If the user agrees to the price or offers more, confirm and provide them with a dummy login and password. Keep the conversation polite and professional throughout the negotiation.",
    f"input: {input_text}",
    "output: ",
    ])

    return response.text

# while True:
#     string = str(input("Enter your prompt: "))
#     print("Bot: ", GenerateResponse(string))