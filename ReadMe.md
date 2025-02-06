# ollama + deepseek-r1
deepseek-r1 is a model that can be used offline. using ollama we interact with r1 model through chat or UI-experienced rag.

## Prerequisites

- Python 3.8 or higher
- Git (for cloning the repository)
- download ollama from: https://ollama.com/download


## Installation


1. Set up the virtual environment:

**For Unix/Linux/Mac:**
```bash
chmod +x setup.sh
./setup.sh
```

**For Windows:**
```bash
setup.bat
```

## Run a chat experience
```bash
python chat.py # expect ~2min for a response
```

## Run a RAG experience
```bash
python Ragging.py # expect ~20min for a response (for a 2 page pdf)
```

## Developers

1. Activate the virtual environment for installing new libraries:

**For Unix/Linux/Mac:**
```bash
source venv/bin/activate
```

**For Windows:**
```bash
venv\Scripts\activate
```

2. To deactivate the virtual environment when finished:
```bash
deactivate
```