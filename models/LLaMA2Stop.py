from peft import PeftModel, PeftConfig
from transformers import AutoModelForCausalLM, AutoTokenizer, Conversation, pipeline

# Load the model
config = PeftConfig.from_pretrained("irlab-udc/LLaMA2-13b-Stop-Hate")
base_model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-13b-chat-hf")
model = PeftModel.from_pretrained(base_model, "irlab-udc/LLaMA2-13b-Stop-Hate")
tokenizer = AutoTokenizer.from_pretrained("irlab-udc/LLaMA2-13b-Stop-Hate")

# Test the model
chatbot = pipeline(task="conversational", model=model, tokenizer=tokenizer)
conversation = Conversation("Your input text here")
conversation = chatbot(conversation)
result = conversation.messages[-1]["content"]
print(result)
