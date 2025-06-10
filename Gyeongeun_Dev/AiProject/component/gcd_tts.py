import os
from google.cloud import texttospeech
from utils.config import read_api_key_path

# 서비스 계정 키 파일 경로 설정
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/apiKey/google-api-key.json"
# 현재 파일 위치 기준 절대경로 생성
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# GOOGLE_KEY_PATH = os.path.join(BASE_DIR, "apiKey/google-api-key.json")
# json_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "apiKey/google-api-key.json")
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = json_path

# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_KEY_PATH

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = read_api_key_path("apiKey/google-api-key.json")


# 클라이언트 초기화
client = texttospeech.TextToSpeechClient()

def synthesize_speech(text: str) -> bytes:
    # 변환할 텍스트 입력
    # text_input = texttospeech.SynthesisInput(text="안녕하세요, 구글 클라우드 텍스트 투 스피치입니다.")
    text_input = texttospeech.SynthesisInput(text=text)

    # 목소리 설정 (언어 코드, 성별 등)
    voice = texttospeech.VoiceSelectionParams(
        language_code="ko-KR",  # 한국어
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL  # 중립적인 음성
    )

    # 오디오 형식 설정
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3  # MP3 형식으로 저장
    )

    # 변환 요청
    response = client.synthesize_speech(
        input=text_input,
        voice=voice,
        audio_config=audio_config
    )

    # 테스트 결과 저장 폴더
    output_dir = "testResults"  # 원하는 폴더명
    os.makedirs(output_dir, exist_ok=True)  # 폴더 없으면 생성

    # 결과 저장
    with open(os.path.join(output_dir, "output.mp3"), "wb") as out:
        out.write(response.audio_content)
        print("✅ 음성 파일이 'output.mp3'로 저장되었습니다.")
    
    return response.audio_content
