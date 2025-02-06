@echo off

:: Create virtual environment
python -m venv venv

:: Activate virtual environment
call venv\Scripts\activate

:: Install required packages
pip install -r requirements.txt

:: Run Ollama with DeepSeek-R1 model
ollama run deepseek-r1
