import json
import os
from openai import OpenAI
from langchain_core.prompts import PromptTemplate
from prompts import search_prompt_system, relevant_prompt_system
from dotenv import load_dotenv
import os 

load_dotenv()
# use ENV variables
MODEL = os.getenv("VLLM_MODEL")

OPENAI_BASE_URL = os.getenv("VLLM_API_URL")
OPENAI_API_KEY = os.getenv("VLLM_API_KEY") 

client = OpenAI(
        api_key=OPENAI_API_KEY, 
        base_url=OPENAI_BASE_URL,
    )

def get_answer(query, contexts):
    # system_prompt_search = PromptTemplate(input_variables=["date_today"], template=search_prompt_system)

    messages = [
        {"role": "system", "content": search_prompt_system},
        {"role": "user", "content": "User Question : " + query + "\n\n CONTEXTS :\n\n" + contexts}
    ]

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            stop=None,
        )
        return response.choices[0].message.content

    except Exception as e:
        print(f"Error during get_answer_groq call: {e}")
        return json.dumps({'type': 'error', 'data': "We are currently experiencing some issues. Please try again later."})


def get_relevant_questions(contexts, query):
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system",
                 "content": relevant_prompt_system
                 },
                {"role": "user",
                 "content": "User Query: " + query + "\n\n" + "Contexts: " + "\n" + contexts + "\n"}
            ],
            response_format={"type": "json_object"},
        )

        return response.choices[0].message.content
    except Exception as e:
        print(f"Error during RELEVANT GROQ ***************: {e}")
        return {}


if __name__ == "__main__":
    print(get_relevant_questions("what's going on? ", "Hello"))