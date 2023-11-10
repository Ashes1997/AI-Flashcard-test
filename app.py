from chatGPT import flash_create

prompt = "Object inheritance in Java is where an object inherits methods and attributes from it's super class"

flashcard = flash_create(prompt)
for f in flashcard:
  print(f)