import requests
import json

# Translator API
API_URL = "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-es-en"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
 
def translate(text_to_translate):
  output = query({
	"inputs": text_to_translate,
  })
  return output


if __name__ == "__main__":
	text_to_translate = "Ha abandonado a sus médicos, señora; bajo cuyo prácticas ha perseguido el tiempo con esperanza, y no encuentra otra ventaja en el proceso sino sólo la perdiendo la esperanza por el tiempo."


	translated= translate(text_to_translate)

	print(translated)

