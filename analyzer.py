import os
from google import genai
from dotenv import load_dotenv
from prompts import resume_prompt

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def analyze_resume(resume_text):

    prompt = resume_text + "\n\n" + resume_prompt

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text




