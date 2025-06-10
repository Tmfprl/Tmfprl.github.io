from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from component.gcd_vision import extract_text_from_image, extract_text_from_image_test
from component.openai_llm import preprocess_text_with_gpt
from component.gcd_tts import synthesize_speech
import io
import uvicorn

api = FastAPI()

# 서비스 제공 api
@api.post("/process/")
async def process_image(file: UploadFile = File(...)):
    image_bytes = await file.read()
    
    # 1. OCR 호출
    extracted_text = extract_text_from_image(image_bytes)
    if not extracted_text:
        return {"error": "OCR 결과 없음"}

    # 2. GPT 호출
    processed_text = preprocess_text_with_gpt(extracted_text)

    # 3. TTS 호출
    audio_bytes = synthesize_speech(processed_text)

    # 4. 응답 호출
    return StreamingResponse(io.BytesIO(audio_bytes), media_type="audio/mpeg")

# 서버 실행
if __name__ == "__main__":
    uvicorn.run("main:api", host="0.0.0.0", port=8000, reload=True)
