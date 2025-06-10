import io
import os
import json
from google.cloud import vision
from google.protobuf.json_format import MessageToDict  # JSON 변환 모듈
from utils.config import read_api_key_path

# 1. 서비스 계정 인증 설정 
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "apiKey/google-api-key.json"

# json_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "apiKey/google-api-key.json")
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = json_path

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = read_api_key_path("apiKey/google-api-key.json")

# 2. Vision API 클라이언트 생성
client = vision.ImageAnnotatorClient()

# 실제 api 호출시 실행되는 코드
def extract_text_from_image(image_bytes: bytes) -> str:
    image = vision.Image(content=image_bytes)
    response = client.document_text_detection(image=image)
    
    if response.text_annotations:
        return response.text_annotations[0].description
    return ""

# 호출시 결과 확인용 테스트 코드2
def extract_text_from_image_test():
    # 3. OCR 적용할 이미지 경로
    # image_path = "content/sample-image.jpeg"  # ✅ OCR 적용할 이미지
    image_path = "content/n-sample-image.jpg"  # ✅ OCR 적용할 이미지

    # 4. 이미지 로드 ("rb"는 파이썬의 open() 함수에서 사용되는 파일 열기 모드, read binary)
    with io.open(image_path, "rb") as image_file:
        content = image_file.read()
        
    image = vision.Image(content=content)

    # 5. OCR 요청 (문서 내 텍스트 검출)
    response = client.document_text_detection(image=image)

    # 6. OCR 결과 추출 및 출력
    if response.text_annotations:
        extracted_text = response.text_annotations[0].description  # ✅ 전체 텍스트 가져오기
        print("\n🔹 Extracted OCR Text:\n")
        print(extracted_text)  

        # 7. JSON 변환 후 저장
        response_dict = MessageToDict(response._pb)  # ✅ `_pb` 사용하여 변환

        # 8. 결과 저장 경로 지정
        output_dir = "testResults"  # 원하는 폴더명
        os.makedirs(output_dir, exist_ok=True)  # 폴더 없으면 생성
        # 9. 텍스트 결과 저장
        with open(os.path.join(output_dir, "ocr_result.txt"), "w", encoding="utf-8") as text_file:
            text_file.write(extracted_text)
        print(f"\n✅ OCR 텍스트 저장 완료: {output_dir}/ocr_result.txt")

        # 10. JSON 결과 저장
        with open(os.path.join(output_dir, "ocr_result.json"), "w", encoding="utf-8") as json_file:
            json.dump(response_dict, json_file, indent=4, ensure_ascii=False)
        print(f"\n✅ OCR 결과 JSON 저장 완료: {output_dir}/ocr_result.json")
        
    else:
        print("\n❌ OCR 결과 없음")

