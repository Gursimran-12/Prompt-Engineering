import requests

# Replace this with your actual Hugging Face API token
API_TOKEN = ("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")

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3.5-large"
HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Accept": "image/png",  # Expecting an image in return
    "Content-Type": "application/json"
}

def generate_image(prompt: str, output_path: str = "output.png"):
    payload = {
        "inputs": prompt
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)

    if response.status_code == 200:
        with open(output_path, "wb") as f:
            f.write(response.content)
        print(f"✅ Image saved as {output_path}")
    else:
        print(f"❌ Failed to generate image. Status code: {response.status_code}")
        print(response.text)

# Example usage
if __name__ == "__main__":
    prompt_text = input("Enter your image prompt: ")
    generate_image(prompt_text)
