import openai

client = openai.OpenAI(api_key="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")

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "너는 도움이 되는 AI야."},
        {"role": "user", "content": "GPT-4o 안녕, 날씨에 대해 알려줘."}
    ]
)

print(response.choices[0].message.content)