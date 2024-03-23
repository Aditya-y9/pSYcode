from transformers import GPT2Tokenizer, TFGPT2Model
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = TFGPT2Model.from_pretrained('gpt2')
text = "make a marketing strategy for a new product launch"
encoded_input = tokenizer(text, return_tensors='tf')
output = model(encoded_input)
