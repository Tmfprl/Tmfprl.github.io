# AiProject - Voice-based Lecture Generator


## 📌 Description
This is a personal project conducted during the **Python Programming Practice** course in the first semester of 2025.  
The application generates **voice-based lecture content** from lecture notes.

**Workflow**  
1. Preprocess lecture note images uploaded by the user using **GCP Vision OCR**.  
2. Expand the recognized text into explanatory material using **OpenAI GPT-4o**.  
3. Convert the final text into audio using **GCP Text-to-Speech (TTS)** and output as a `.mp3` file.  

- **Language**: Python  
- **IDE**: Visual Studio Code  
- **Development Time**: ~1 week  

---

## ✨ Features
- Extract text from lecture notes or images (OCR)  
- Generate explanatory text with GPT-4o  
- Convert text into audio lectures using Google Cloud TTS  
- Output final lecture as an `.mp3` audio file  

---

## 🛠️ Tech Stack
| Component | Technology |
|-----------|------------|
| OCR       | Google Cloud Vision |
| LLM       | OpenAI GPT-4o |
| TTS       | Google Cloud Text-to-Speech |
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
├─ main.py               # Entry point
├─ requirements.txt      # Python dependencies
├─ testResults
│  └─ output.mp3         # Example generated audio
└─ utils
└─ config.py             # Configuration (API keys, paths, etc.)

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

A sample generated audio file is available at:
`testResults/output.mp3`

---

## 📜 License

This project is licensed under the MIT License.

---

## 👩‍💻 Author

Developed by GYEONGEUN PARK (First semester, 4th year, 2025)

Course: *Python Programming Practice*

---
KOREAN.ver
# AiProject - 음성 기반 강의 생성기


## 📌 프로젝트 설명
이 프로젝트는 2025년 1학기 **파이썬 프로그래밍 실무** 강의에서 진행한 개인 프로젝트입니다.  
사용자의 강의 정리본 이미지를 기반으로 **음성 형태의 강의 자료**를 생성하는 애플리케이션입니다.

**워크플로우**  
1. 사용자가 업로드한 강의 정리본 이미지를 **GCP Vision OCR**로 전처리  
2. 인식된 텍스트를 **OpenAI GPT-4o**로 설명 자료로 확장  
3. 최종 텍스트를 **GCP Text-to-Speech (TTS)**로 변환하여 `.mp3` 파일로 출력  

- **언어**: Python  
- **IDE**: Visual Studio Code  
- **개발 기간**: 약 1주

---

## ✨ 주요 기능
- 강의 노트/이미지에서 텍스트 추출 (OCR)  
- GPT-4o를 활용한 설명 텍스트 생성  
- Google Cloud TTS를 이용한 텍스트 → 음성 변환  
- 최종 강의를 `.mp3` 오디오 파일로 제공

---

## 🛠️ 기술 스택
| 구성 요소 | 기술 |
|-----------|------------|
| OCR       | Google Cloud Vision |
| LLM       | OpenAI GPT-4o |
| TTS       | Google Cloud Text-to-Speech |
| 언어      | Python |
| IDE       | VSCode |

---

## 📂 프로젝트 구조
```

AiProject
├─ .DS\_Store
├─ component
│  ├─ gcd\_tts.py         # Google Cloud TTS 모듈
│  ├─ gcd\_vision.py      # Google Cloud Vision (OCR) 모듈
│  └─ openai\_llm.py      # OpenAI GPT-4o 연동
├─ content
│  ├─ n-sample-image.jpg # 예제 입력 이미지
│  └─ sample-image.jpeg  # 예제 입력 이미지
├─ main.py               # 실행 진입점
├─ requirements.txt      # Python 의존성
├─ testResults
│  └─ output.mp3         # 생성된 오디오 예제
└─ utils
└─ config.py             # 환경 설정 (API 키, 경로 등)

````

---

## ⚙️ 설치 방법
```bash
git clone https://github.com/Tmfprl/Tmfprl.github.io.git
cd Gyeongeun_Dev/AiProject
pip install -r requirements.txt
````

**환경 설정**

* Google Cloud 인증 정보 설정:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="path/to/your-gcp-key.json"
```

* OpenAI API 키 설정:

```bash
export OPENAI_API_KEY="your-openai-api-key"
```

---

## 🚀 사용 방법

샘플 이미지를 이용해 메인 스크립트 실행:

```bash
python main.py --input ./content/sample-image.jpeg --output ./testResults/output.mp3
```

---

## 🎧 예제 출력

샘플 생성 오디오 파일 위치:
`testResults/output.mp3`

---

## 📜 라이선스

이 프로젝트는 **MIT License** 하에 배포됩니다.

---

## 👩‍💻 개발자

개발자: GYEONGEUN PARK (2025년 1학기 4학년)

강의: *파이썬 프로그래밍 실무*


