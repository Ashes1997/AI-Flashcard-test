import openai
import os
from openai import OpenAI

client = OpenAI()
flashcard = "SQL queries using select, where, group by and having clauses utilise the where clause first, then group by, then select, then having"

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a tutor that creates flashcards for your students in the following format. Question:.......... /n/n Answer:........... , The questions and answers are based off the submitted text and should be no longer than 50 words each. You rely heavily on the given text and rely little on external information. Reply with only one question, one correct answer, and 3 incorrect answers with false details."},
    {"role": "user", "content": flashcard}
  ]
)

#print(completion.choices[0].message)
print(completion.choices[0])