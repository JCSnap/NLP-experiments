from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("gpt2")

encoded = tokenizer.encode("Hello, I'm a single sentence!")

print(encoded)

output = tokenizer.convert_ids_to_tokens(encoded[0], skip_special_tokens=False)
for i in range(1, len(encoded)):
    output += tokenizer.convert_ids_to_tokens(encoded[i], skip_special_tokens=False)

print(output)

