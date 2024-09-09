import openai
from dotenv import load_dotenv
import os 
import requests 
load_dotenv()


OPENAI_BASE_URL = os.getenv("VLLM_API_URL") # Note the /v1 at the end
OPENAI_API_KEY = os.getenv("VLLM_API_KEY") # Make sure to replace with the right one

SYSTEM_PROMPT = "You are a helpful AI assistant"
TEST_PROMPT = "What is Entropy?"


if __name__ == "__main__":

    # response = requests.get(OPENAI_BASE_URL + "/v1/models",headers={"Authorization": f"Bearer {OPENAI_API_KEY}"})
    # print(response.json())

    client = openai.OpenAI(
        api_key=OPENAI_API_KEY, 
        base_url=OPENAI_BASE_URL,
    )

    response = client.chat.completions.create(
        model="NousResearch/Meta-Llama-3-8B-Instruct",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": TEST_PROMPT}
        ],
    )

    print(response.choices[0].message.content)


