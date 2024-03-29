from openai import OpenAI
client = OpenAI()

def parse(user_in):
  print("Querying ChatGPT")
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "Provide only the parameters for the values of m (mass of object), vi (initial velocity), ti (initial time), tf (final time), g (gravitational acceleration), in JSON format. Leave a field empty if the information is not provided and omit units. Values going down (e.g. gravitational acceleration) should be negative, and vice versa."},
      {"role": "user", "content": user_in}
    ]
  )

  print(completion.choices[0].message)