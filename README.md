# Jupyter Notebook Translator

## 📝 프로젝트 소개
Jupyter Notebook Translator는 Jupyter 노트북(.ipynb) 파일의 마크다운 셀을 다양한 언어로 번역할 수 있는 웹 애플리케이션입니다. Streamlit 기반의 간단한 UI를 통해 사용자는 파일 업로드부터 번역, 다운로드까지 손쉽게 사용할 수 있습니다.

## 🚀 주요 기능
- Jupyter Notebook 파일 업로드 및 번역
- 마크다운 셀의 이미지 마크다운 자동 감지 및 보존
- 번역 진행률 표시(프로그레스 바 및 셀 카운트)
- 번역 완료된 파일의 로컬 다운로드 기능
- 다양한 언어 지원 (영어, 한국어, 프랑스어, 독일어, 스페인어, 중국어 간체, 일본어)

## 🧩 사용된 기술
- **프로그래밍 언어:** Python
- **웹 프레임워크:** Streamlit
- **번역 API:** deep-translator (GoogleTranslator)
- **기타 라이브러리:** json, os, io, re, time, pathlib

## 💾 설치 및 실행 방법
### 1. 사전 조건
- Python 3.8 이상이 설치되어 있어야 합니다.

### 2. 프로젝트 클론
```bash
# GitHub 레포지토리 클론
git clone https://github.com/username/jupyter-notebook-translator.git
cd jupyter-notebook-translator
```

### 3. 가상 환경 생성 및 활성화
```bash
# 가상 환경 생성 (Windows)
python -m venv venv

# 가상 환경 활성화 (Windows)
venv\\Scripts\\activate

# 가상 환경 활성화 (Mac/Linux)
source venv/bin/activate
```

### 4. 의존성 패키지 설치
```bash
pip install -r requirements.txt
```

### 5. 애플리케이션 실행
```bash
streamlit run app.py
```

## 📁 프로젝트 구조
```plaintext
jupyter-notebook-translator
├── app.py                 # 메인 애플리케이션 코드
├── requirements.txt       # 의존성 패키지 목록
└── README.md              # 프로젝트 설명 파일
```

## 🌱 기여 방법
1. 해당 레포지토리를 포크(Fork)합니다.
2. 새로운 브랜치를 생성합니다. (`git checkout -b feature-new-functionality`)
3. 변경 사항을 커밋합니다. (`git commit -m 'Add new feature'`)
4. 브랜치에 푸시합니다. (`git push origin feature-new-functionality`)
5. Pull Request를 생성합니다.

## 📜 라이선스
이 프로젝트는 MIT 라이선스에 따라 사용할 수 있습니다.

## 🌍 다국어 지원
- [English](README_EN.md)
- [한국어](README.md)

## 💡 추가 설명
- 이 프로젝트는 데이터 과학자와 연구자가 다국어 환경에서도 Jupyter Notebook을 효과적으로 사용할 수 있도록 돕습니다.
- 향후에는 코드 셀의 주석도 번역할 수 있는 기능을 추가할 계획입니다.

---

![Streamlit Logo](https://docs.streamlit.io/en/stable/_static/favicon.png)

