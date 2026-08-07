import os

from groq import Groq

import app

client = Groq(api_key=(os.getenv("GROQ_API_KEY")))

customer_name = input("Enter customer name: ")
customer_order = input("Enter customer order: ")
customer_quantity = int(input("Enter customer quantity: "))

#step 1: Create a prompt
prompt = f"""
customer name: {customer_name}
customer order: {customer_order}
customer quantity: {customer_quantity}
please provide a summary of the customer order is healthy or not.
"""
#step 2:
response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

response_text = response.choices[0].message.content
print(response_text)

