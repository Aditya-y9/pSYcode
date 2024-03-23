from transformers import T5ForConditionalGeneration, T5Tokenizer

# Define the Gemma model name
model_name = "t5-large"

# Load the Gemma model and tokenizer
model = T5ForConditionalGeneration.from_pretrained(model_name)
tokenizer = T5Tokenizer.from_pretrained(model_name)

def generate_output(input_text):
    # Tokenize input text
    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    # Generate output from the Gemma model
    output_ids = model.generate(input_ids)

    # Decode the output
    output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return output_text

# Input text
input_text = "Generate marketing strategy for computer software company, which includes market research, target audience, and marketing channels."

# Generate and print the output
output_text = generate_output(input_text)
print("Output:", output_text)
