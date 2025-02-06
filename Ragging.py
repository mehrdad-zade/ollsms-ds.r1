import gradio as gr
import re
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
import ollama

'''
Loads and prepares PDF content for retrieval-based answering.
Checks if a PDF is uploaded.
Extracts text using PyMuPDFLoader.
Splits text into chunks using RecursiveCharacterTextSplitter.
Generates vector embeddings using OllamaEmbeddings.
Stores embeddings in a Chroma vector store for efficient retrieval.
'''
def process_pdf(pdf_bytes):
    if pdf_bytes is None:
        return None, None, None

    loader = PyMuPDFLoader(pdf_bytes)
    data = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500, chunk_overlap=100
    )
    chunks = text_splitter.split_documents(data)

    embeddings = OllamaEmbeddings(model="deepseek-r1")  
    vectorstore = Chroma.from_documents(
        documents=chunks, embedding=embeddings, persist_directory="./chroma_db"
    )
    retriever = vectorstore.as_retriever()

    return text_splitter, vectorstore, retriever

'''
Since retrieval-based models pull relevant excerpts rather than entire documents,
this function ensures that the extracted content remains readable and properly formatted
before being passed to DeepSeek-R1.
'''
def combine_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


'''
First searches the vector store using retriever.invoke(question), returning the most
relevant document excerpts. These excerpts are formatted into a structured input using
combine_docs function and sent to ollama_llm, ensuring that DeepSeek-R1 generates
well-informed answers based on the retrieved content.
'''
def rag_chain(question, text_splitter, vectorstore, retriever):
    retrieved_docs = retriever.invoke(question)
    formatted_content = combine_docs(retrieved_docs)
    return ollama_llm(question, formatted_content)

'''
Querying DeepSeek-R1 using Ollama
'''
def ollama_llm(question, context):
    formatted_prompt = f"Question: {question}\n\nContext: {context}"

    response = ollama.chat(
        model="deepseek-r1",
        messages=[{"role": "user", "content": formatted_prompt}],
    )

    response_content = response["message"]["content"]

    # Remove content between <think> and </think> tags to remove thinking output
    final_answer = re.sub(r"<think>.*?</think>", "", response_content, flags=re.DOTALL).strip()

    return final_answer

# process PDF input and ask questions related to it.
def ask_question(pdf_bytes, question):
    text_splitter, vectorstore, retriever = process_pdf(pdf_bytes)

    if text_splitter is None:
        return None  # No PDF uploaded

    result = rag_chain(question, text_splitter, vectorstore, retriever)
    return result  # Fixed incorrect return type

interface = gr.Interface(
    fn=ask_question,
    inputs=[
        gr.File(label="Upload PDF (optional)"),
        gr.Textbox(label="Ask a question"),
    ],
    outputs="text",
    title="Ask questions about your PDF",
    description="Use DeepSeek-R1 to answer your questions about the uploaded PDF document.",
)

interface.launch()
