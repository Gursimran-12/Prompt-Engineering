import google.generativeai as genai

# Configure API key
genai.configure(api_key="AIzaSyCinnrFJHds_HUj5IsFx5_8_mp4ksJs8MA")

# Use Gemini Flash
model = genai.GenerativeModel("gemini-1.5-flash")

# Two different prompts to test
prompt_a = "Explain to school students why they should read books, using simple examples."
prompt_b = "Why is reading important for kids? Explain in child-friendly language."

# Generate both responses
response_a = model.generate_content(prompt_a)
response_b = model.generate_content(prompt_b)

# Display both for manual judgment
print("🟥 Prompt A Output:\n", response_a.text, "\n")
print("🟦 Prompt B Output:\n", response_b.text, "\n")

# Ask for human input
choice = input("👉 Which response do YOU think is better? (A/B): ")

if choice.strip().upper() == "A":
    print("✅ You selected Prompt A.")
elif choice.strip().upper() == "B":
    print("✅ You selected Prompt B.")
else:
    print("❌ Invalid input.")
