from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
import os

model_name = "mistralai/Mistral-Small-3.1-24B-Instruct-2503"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Save model and tokenizer
model_dir = "./hf_model"
os.makedirs(model_dir, exist_ok=True)
model.save_pretrained(model_dir)
tokenizer.save_pretrained(model_dir)