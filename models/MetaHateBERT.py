from transformers import pipeline

# Load the model
classifier = pipeline("text-classification", model="irlab-udc/MetaHateBERT")

# Test the model
result = classifier("Your input text here")
print(result)  # Should print the labels "no hate" or "hate"
