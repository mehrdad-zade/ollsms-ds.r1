#!/bin/bash

# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install required packages
pip install -r requirements.txt

echo "Setup complete! To activate the environment, run: source venv/bin/activate"

# Run Ollama with DeepSeek-R1 model
ollama run deepseek-r1
