FROM vllm/vllm-openai:latest

WORKDIR /app
COPY requirements.txt /app/requirements.txt /app/
RUN pip install -r requirements.txt
CMD ["--model", "unsloth/llama-3-8b-Instruct-bnb-4bit", "--max-model-len", "8192", "--port", "8000"]

