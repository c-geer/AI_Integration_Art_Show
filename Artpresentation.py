import requests
import os
from openai import OpenAI
from elevenlabs import ElevenLabs

## Generate text using perpelexity
def generateresponse(input: str):

    API_KEY = os.environ.get('PERPLEXITY_API_KEY')

    messages = [
        {
            "role": "system",
            "content": (
                "You are an artificial intelligence assistant and you need to "
                "engage in a helpful, detailed, polite conversation with a user."
            ),
        },
        {   
            "role": "user",
            "content": (
                input
            ),
        },
    ]

    client = OpenAI(api_key=API_KEY, base_url="https://api.perplexity.ai")

    response = client.chat.completions.create(
        model="llama-3.1-sonar-large-128k-online",
        messages=messages,
    )
    print(response)


## Generate an image with Dall-e-3"
def generateimage(input: str):
  client = OpenAI()
  response = client.images.generate(
    model="dall-e-3",
    prompt= input,
    size="1024x1024",
    quality="standard",
    n=1,
    )
  image_url = response.data[0].url
  print(image_url)
  print()


## Generate a sound effect
def generate_sound_effect(text: str, output_path: str):
    elevenlabs = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))
    print("Generating sound effects...")

    result = elevenlabs.text_to_sound_effects.convert(
        text=text,
        duration_seconds=10, 
        prompt_influence=0.3,  
    )

    with open(output_path, "wb") as f:
        for chunk in result:
            f.write(chunk)

    print(f"Audio saved to {output_path}")


if __name__ == "__main__":
    generate_sound_effect("Cold winds whippinga and ice crackling.", "Arctic.mp3")
    generateimage("An arctic landscape with wildlife.")
    generateresponse("Give me facts about arctic ecosystems.")
    generateresponse("Give me a list of biodiversity found in arctic ecosystems.")


