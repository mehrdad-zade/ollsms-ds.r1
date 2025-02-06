# ollama + deepseek r1
deepseek-r1 is a model that can be used offline. using ollama we interact with r1 model through chat or UI-experienced rag.

## Prerequisites

- Python 3.11.9: https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe
- download ollama from: https://ollama.com/download
- install Git: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
- pip

## Installation

1.  Download the package

```bash
git clone git@github.com:mehrdad-zade/ollsms-ds.r1.git
cd ollsms-ds.r1
```

2. Set up:

**For Unix/Linux/Mac:**
```bash
chmod +x setup.sh
./setup.sh
```

**For Windows:**
```bash
.\setup.bat
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