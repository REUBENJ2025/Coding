from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# ----- 1. Load model -----
model_name = "meta-llama/Llama-2-7b-chat-hf"  # LLaMA 2 Chat model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",          # automatically use GPU if available
    torch_dtype=torch.float16   # use half precision for memory efficiency
)

# ----- 2. Initialize chat history -----
# Inject the current year to make AI always respond correctly
history = "Assistant: The current year is 2025.\n"

print("Type 'quit' to exit.\n")

# ----- 3. Chat loop -----
while True:
    user_input = input("You: ")
    if user_input.strip().lower() == "quit":
        break

    # Add user input to history
    history += f"User: {user_input}\nAssistant:"

    # Encode input for model
    inputs = tokenizer(history, return_tensors="pt").to("cuda" if torch.cuda.is_available() else "cpu")

    # Generate response
    output = model.generate(
        **inputs,
        max_new_tokens=200,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        top_p=0.9,
        temperature=0.7
    )

    # Decode and extract assistant response
    reply = tokenizer.decode(output[0], skip_special_tokens=True)
    assistant_text = reply.split("Assistant:")[-1].strip()

    # Print and update history
    print("AI:", assistant_text)
    history += f" {assistant_text}\n"
