from peft import PeftModel, PeftConfig
from transformers import AutoModelForCausalLM, AutoTokenizer, Conversation, pipeline

# Load the model
config = PeftConfig.from_pretrained("ARR/LLaMA2Stop")
base_model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-13b-chat-hf", config=config)
model = PeftModel.from_pretrained(base_model, "ARR/LLaMA2Stop")
tokenizer = AutoTokenizer.from_pretrained("ARR/LLaMA2Stop")

# Test the model
chatbot = pipeline(task="conversational", model=model, tokenizer=tokenizer)
conversation = Conversation("Your input text here")
conversation = chatbot(conversation)
result = conversation.messages[-1]["content"]
print(result)

