# Jupyter Notebook Translator

## 📝 Project Introduction
Jupyter Notebook Translator is a web application that translates the markdown cells of Jupyter Notebook (.ipynb) files into various languages. With a simple UI built on Streamlit, users can easily upload, translate, and download files.

## 🚀 Key Features
- Upload and translate Jupyter Notebook files
- Automatic detection and preservation of image markdown in cells
- Translation progress display (progress bar and cell count)
- Local download of the translated file
- Supports multiple languages (English, Korean, French, German, Spanish, Simplified Chinese, Japanese)

## 🧩 Technologies Used
- **Programming Language:** Python
- **Web Framework:** Streamlit
- **Translation API:** deep-translator (GoogleTranslator)
- **Other Libraries:** json, os, io, re, time, pathlib

## 💾 Installation and Execution
### 1. Prerequisites
- Python 3.8 or higher must be installed.

### 2. Clone the Project
```bash
# Clone the GitHub repository
git clone https://github.com/username/jupyter-notebook-translator.git
cd jupyter-notebook-translator
```

### 3. Create and Activate a Virtual Environment
```bash
# Create a virtual environment (Windows)
python -m venv venv

# Activate the virtual environment (Windows)
venv\\Scripts\\activate

# Activate the virtual environment (Mac/Linux)
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the Application
```bash
streamlit run app.py
```

## 📁 Project Structure
```plaintext
jupyter-notebook-translator
├── app.py                 # Main application code
├── requirements.txt       # List of dependencies
└── README_EN.md           # Project documentation (English)
```

## 🌱 Contribution Guidelines
1. Fork this repository.
2. Create a new branch (`git checkout -b feature-new-functionality`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-new-functionality`).
5. Create a Pull Request.

## 📜 License
This project is licensed under the MIT License.

## 🌍 Multi-language Support
- [English](README_EN.md)
- [Korean](README.md)

## 💡 Additional Information
- This project helps data scientists and researchers effectively use Jupyter Notebooks in multilingual environments.
- Future updates will include the ability to translate comments within code cells.

---

![Streamlit Logo](https://docs.streamlit.io/en/stable/_static/favicon.png)

