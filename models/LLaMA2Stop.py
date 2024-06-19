import torch
from peft import PeftModel, PeftConfig
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, Conversation, pipeline

# Load the model
base_model_id = "meta-llama/Llama-2-13b-chat-hf"
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16
)
model = AutoModelForCausalLM.from_pretrained(base_model_id, quantization_config=bnb_config)
tokenizer = AutoTokenizer.from_pretrained(
    base_model_id,
    model_max_length=512,
    padding_side="left",
    add_eos_token=True,
    add_bos_token=True)
tokenizer.pad_token = tokenizer.eos_token
ft_model = PeftModel.from_pretrained(model, "/LLaMA2Stop")

# Test the model
chatbot = pipeline(task="conversational", model=ft_model, tokenizer=tokenizer)
conversation = Conversation("Your input text here")
conversation = chatbot(conversation)
result = conversation.messages[-1]["content"]
print(result)
