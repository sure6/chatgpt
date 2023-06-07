import os
import openai

openai.api_key = "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"

# response_qa = openai.Completion.create(
#   model="text-davinci-003",
#   prompt="Q: Which company is Epic game\nA:",
#   temperature=0,
#   max_tokens=100,
#   top_p=1,
#   frequency_penalty=0.0,
#   presence_penalty=0.0,
#   stop=["\n"]
# )
#
# response_grammer_correction = openai.Completion.create(
#   model="text-davinci-003",
#   prompt="Correct this to standard English:\n\nShe no went to the market.",
#   temperature=0,
#   max_tokens=60,
#   top_p=1.0,
#   frequency_penalty=0.0,
#   presence_penalty=0.0
# )
#
# response_translation = openai.Completion.create(
#   model="text-davinci-003",
#   prompt="Translate this into 1. French, 2. Spanish and 3. Japanese:\n\nWhat rooms do you have available?\n\n1.",
#   temperature=0.3,
#   max_tokens=100,
#   top_p=1.0,
#   frequency_penalty=0.0,
#   presence_penalty=0.0
# )

response_create_study_notes = openai.Completion.create(
  model="text-davinci-003",
  prompt="what is Apache spark",
  temperature=0.3,
  max_tokens=150,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

# response_image_generation = openai.Image.create(prompt="",n=1,size="1024x1024")
# image_url = response_image_generation['data'][0]['url']
# print(image_url)

# print(response_translation)
# print(response_grammer_correction)
# print(response_qa)
print(response_create_study_notes)