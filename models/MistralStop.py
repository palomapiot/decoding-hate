from peft import PeftModel, PeftConfig
from transformers import AutoModelForCausalLM, AutoTokenizer, Conversation, pipeline

# Load the model
config = PeftConfig.from_pretrained("ARR/MistralStop")
base_model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2", config=config)
model = PeftModel.from_pretrained(base_model, "ARR/MistralStop")
tokenizer = AutoTokenizer.from_pretrained("ARR/MistralStop")

# Test the model
chatbot = pipeline(task="conversational", model=model, tokenizer=tokenizer)
conversation = Conversation("Your input text here")
conversation = chatbot(conversation)
result = conversation.messages[-1]["content"]
print(result)
