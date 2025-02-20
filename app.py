import streamlit as st
import json
import os
from io import BytesIO
import re
from deep_translator import GoogleTranslator
from pathlib import Path
import time

def translate_markdown_cells(nb_data, src_lang, dest_lang):
    translator = GoogleTranslator(source=src_lang, target=dest_lang)
    
    # 프로그레스 바 초기화
    total_cells = sum(1 for cell in nb_data["cells"] if cell["cell_type"] == "markdown")
    progress_bar = st.progress(0)
    progress_text = st.empty()  # 진행률 표시용
    
    processed_cells = 0
    for cell in nb_data["cells"]:
        if cell["cell_type"] == "markdown":
            text = cell.get("source", None)
            if text:
                if isinstance(text, list):
                    text = ''.join(text)
                
                # 정규식으로 이미지 마크다운 감지
                image_pattern = r"!\[.*?\]\(.*?\)"
                images = re.findall(image_pattern, text)
                
                # 이미지 마크다운을 임시 토큰으로 변경
                placeholders = [f"IMAGEPLACEHOLDER{i}" for i in range(len(images))]
                for img, placeholder in zip(images, placeholders):
                    text = text.replace(img, placeholder)
                
                # 번역수행
                translated_text = translator.translate(text)
                print(translated_text)
                
                # 번역 후 이미지 마크다운 복원
                for placeholder, img in zip(placeholders, images):
                    translated_text = re.sub(re.escape(placeholder), img, translated_text, flags=re.IGNORECASE)
                    print(translated_text)
                    
                cell["source"] = translated_text
                
                # 프로그레스 바 업데이트
                processed_cells += 1
                progress = int((processed_cells / total_cells) * 100)
                progress_bar.progress(progress)
                progress_text.text(f"Translating... {processed_cells}/{total_cells} cells processed ({progress}%)")
                
                # 번역이 빠르게 끝날 경우 시각적으로 표시되도록 약간의 지연 추가 (테스트용)
                time.sleep(0.2)
                

    progress_bar.progress(100)
    progress_text.text("Translation complete!")
    return nb_data



def main():
    st.title("Jupyter Notebook Translator")
    
    # 파일 업로드
    uploaded_file = st.file_uploader("Upload your Jupyter Notebook (.ipynb)", type=["ipynb"])
    
    if uploaded_file is not None:
        nb_data = json.load(uploaded_file)
        
        src_lang = st.selectbox("Select source language", ["en", "ko", "fr", "de", "es", "zh-cn", "ja"])
        dest_lang = st.selectbox("Select target language", ["en", "ko", "fr", "de", "es", "zh-cn", "ja"])
        
        # 사용자 입력으로 파일명 입력
        file_name = st.text_input("Enter the file name for download", value="translated_notebook.ipynb")
        
        # 사용자가 로컬 경로를 입력하도록 함
        save_path = st.text_input("Enter the folder path to save the file", value=str(Path.home()))

        if st.button("Translate and Save"):
            translated_nb = translate_markdown_cells(nb_data, src_lang, dest_lang)
            translated_json = json.dumps(translated_nb, indent=2, ensure_ascii=False)
            
            # 로컬 파일 저장
            save_full_path = os.path.join(save_path, file_name)
            try:
                with open(save_full_path, "w", encoding="utf-8") as f:
                    f.write(translated_json)
                st.success(f"File saved successfully at: {save_full_path}")
            except Exception as e:
                st.error(f"Failed to save the file: {e}")
            
if __name__ == "__main__":
    main()
    # debug
    # uploaded_file = r"C:\Users\user\Desktop\psh\project\ipynb_translator\test\[Notebook - facilitator] Week 6 Public Tenders Romania.ipynb"
    # with open(uploaded_file, "r", encoding="utf-8") as f:
    #     nb_data = json.load(f)
        
    # translated_nb = translate_markdown_cells(nb_data, "en", "ko")
    
    # print(translated_nb)