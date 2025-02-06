@echo off

:: Create virtual environment
python -m venv venv
python -m pip install --upgrade pip

:: Activate virtual environment
call venv\Scripts\activate

:: Install required packages
pip install -r requirements.txt
pip install --upgrade --force-reinstall ollama
pip install --upgrade gradio
pip install --upgrade langchain_community
pip install --upgrade langchain_ollama 

:: Run Ollama with DeepSeek-R1 model
ollama run deepseek-r1
