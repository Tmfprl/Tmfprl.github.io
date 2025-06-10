import openai
import os
from utils.config import read_api_key  # 공통 유틸에서 불러옴

# # 현재 파일의 디렉토리 기준으로 경로 설정
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# API_KEY_PATH = os.path.join(BASE_DIR, "..", "apiKey", "openai-api-key.txt")

# # insert api key 
# # 텍스트 파일에서 API 키 불러오기
# # with open("/apiKey/openai-api-key.txt", "r") as f:
# with open(API_KEY_PATH, "r") as f:
#     api_key = f.read().strip()  # 공백, 개행 제거

api_key = read_api_key("apiKey/openai-api-key.txt")
# client = OpenAI(api_key=api_key)

# 클라이언트 생성
client = openai.OpenAI(api_key=api_key)

def preprocess_text_with_gpt(prompt: str) -> str:
    # 테스트용
    # with open("testResults/ocr_result.txt", "r") as f:
        # prompt = f.read()
        # print(prompt)

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "나는 학생이고 너는 내가 간단하게 적은 정리본에 대해 자세하게 강의하듯이 설명해줘"},
            {"role": "user", "content": prompt}
        ]
    )
    print(response.choices[0].message.content)
    
    return response.choices[0].message.content