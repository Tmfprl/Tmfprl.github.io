import openai

# insert api key 
# 텍스트 파일에서 API 키 불러오기
with open("apiKey/openai-api-key.txt", "r") as f:
    api_key = f.read().strip()  # 공백, 개행 제거

# 클라이언트 생성
client = openai.OpenAI(api_key=api_key)


response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "너는 도움이 되는 AI야."},
        {"role": "user", "content": "GPT-4o 안녕, 날씨에 대해 알려줘."}
    ]
)

print(response.choices[0].message.content)