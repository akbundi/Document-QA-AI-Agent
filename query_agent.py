from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch
import os

# Step 1: Set Hugging Face access token
# Replace this with your actual token or set it via environment variable (recommended)
HF_TOKEN = "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"

# Step 2: Define the gated model
MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

# Step 3: Load tokenizer and model with token
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, token=HF_TOKEN)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float16,
    device_map="auto",
    token=HF_TOKEN
)

# Step 4: Create a text generation pipeline
chatbot = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Step 5: Define your Q&A function
def query_ai(context, question):
    prompt = f"""You are an academic research assistant. Use the following context to answer the question.

Context:
{context}

Question:
{question}

Answer:"""

    result = chatbot(prompt, max_new_tokens=256, do_sample=True, temperature=0.3)
    return result[0]['generated_text'].split("Answer:")[-1].strip()

# Example usage:
# print(query_ai("The mitochondria is the powerhouse of the cell.", "What is the mitochondria?"))
