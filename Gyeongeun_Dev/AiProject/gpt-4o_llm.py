import openai

# insert api key 

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "너는 도움이 되는 AI야."},
        {"role": "user", "content": "GPT-4o 안녕, 날씨에 대해 알려줘."}
    ]
)

print(response.choices[0].message.content)