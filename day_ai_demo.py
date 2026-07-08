from groq import Groq

client = Groq(api_key="my_api_key")

customer_name = "santosh"
customer_order = "Vada"
customer_quantity = 2
customer_bill = 40

#step 1: Create a prompt
prompt = f"""
customer name: {customer_name}
customer order: {customer_order}
customer quantity: {customer_quantity}
customer bill: {customer_bill}
please provide all of above
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
