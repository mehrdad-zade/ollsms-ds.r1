import ollama
import time
import sys
import threading
import re

model_name = "deepseek-r1"
conversation_history = []

def loading_animation(stop_event):
    """Displays a blinking three-dot animation while waiting for a response."""
    while not stop_event.is_set():
        for i in range(4):  # 0, 1, 2, 3
            sys.stdout.write("\rThinking" + "." * i + "   ")  # Print dots
            sys.stdout.flush()
            time.sleep(0.5)
        sys.stdout.write("\rThinking    ")  # Clear line
        sys.stdout.flush()

while True:
    prompt = input("Prompt: ")
    if prompt.lower() == "/bye":
        print("Goodbye!")
        break

    # Append previous responses to maintain conversation context
    conversation_history.append({"role": "user", "content": prompt})

    stop_event = threading.Event()
    loader_thread = threading.Thread(target=loading_animation, args=(stop_event,))
    loader_thread.start()

    response = ollama.chat(
        model=model_name,
        messages=conversation_history,
    )

    stop_event.set()
    loader_thread.join()

    sys.stdout.write("\r" + " " * 20 + "\r")  # Clear the "Thinking..." text
    sys.stdout.flush()

    # Extract content outside of <think>...</think>
    raw_response = response["message"]["content"]
    cleaned_response = re.sub(r"<think>.*?</think>", "", raw_response, flags=re.DOTALL).strip()

    # Append assistant response to history
    conversation_history.append({"role": "assistant", "content": raw_response})

    if cleaned_response:
        print(cleaned_response)
