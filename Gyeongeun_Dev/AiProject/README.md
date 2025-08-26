
# AiProject - Voice-based Lecture Generator

# ** 현재 openAi 및 gcp ai 모델 토큰 만료로 실행되지 않음

## 📌 Description
2025년 1학기 **파이썬프로그래밍실무** 강의에서 진행한 개인 프로젝트입니다.  
강의 정리본을 기반으로 **보이스 형태의 강의 자료**를 생성하는 애플리케이션입니다.  

**Workflow**  
1. 사용자가 입력한 강의 정리본 이미지를 **GCP Vision OCR**로 전처리  
2. 인식된 텍스트를 **OpenAI GPT-4o**로 설명 자료로 확장  
3. 최종 텍스트를 **GCP Text-to-Speech (TTS)**로 변환해 음성 파일 출력  

- **Language**: Python  
- **IDE**: Visual Studio Code  
- **Development Time**: ~1 week  

---

## ✨ Features
- Extract text from lecture notes/images (OCR)
- Generate explanatory text with GPT-4o
- Convert text into audio lectures using Google Cloud TTS
- Provide `.mp3` output as the final lecture

---

## 🛠️ Tech Stack
| Component | Technology |
|-----------|-------------|
| OCR       | Google Cloud Vision |
| LLM       | OpenAI GPT-4o |
| TTS       | Google Cloud TTS |
| Language  | Python |
| IDE       | VSCode |

---

## 📂 Project Structure
```

AiProject
├─ .DS\_Store
├─ component
│  ├─ gcd\_tts.py         # Google Cloud TTS module
│  ├─ gcd\_vision.py      # Google Cloud Vision (OCR) module
│  └─ openai\_llm.py      # OpenAI GPT-4o integration
├─ content
│  ├─ n-sample-image.jpg # Sample input image
│  └─ sample-image.jpeg  # Sample input image
├─ main.py               # Entry point for execution
├─ requirements.txt      # Python dependencies
├─ testResults
│  └─ output.mp3         # Example output audio
└─ utils
└─ config.py          # Configuration (API keys, paths, etc.)

````

---

## ⚙️ Installation
```bash
git clone https://github.com/Tmfprl/Tmfprl.github.io.git
cd Gyeongeun_Dev/AiProject
pip install -r requirements.txt
````

**Environment Setup**

* Set your Google Cloud credentials:

  ```bash
  export GOOGLE_APPLICATION_CREDENTIALS="path/to/your-gcp-key.json"
  ```
* Set your OpenAI API key:

  ```bash
  export OPENAI_API_KEY="your-openai-api-key"
  ```

---

## 🚀 Usage

Run the main script with a sample image:

```bash
python main.py --input ./content/sample-image.jpeg --output ./testResults/output.mp3
```

---

## 🎧 Example Output

A sample generated audio file can be found in:
`testResults/output.mp3`

---

## 📜 License

This project is licensed under the MIT License.

---

## 👩‍💻 Author

Developed by GYEONGEUN PARK (2025 4학년 1학기)

Course: *Python Programming Practice*







