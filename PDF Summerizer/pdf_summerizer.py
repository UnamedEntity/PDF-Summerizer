import os
from dotenv import load_dotenv
import tkinter as tk
from tkinter import filedialog
import PyPDF2

import openai
openai.api_key = input("Enter your OpenAI API key: ")
root = tk.Tk()
root.withdraw()
PDF = filedialog.askopenfilename(
        title="Select a PDF file",
        filetypes=[("PDF files", "*.pdf")])
root.destroy()
def extract_text(PDF):
    with open(PDF, "rb") as f:
        pdf = PyPDF2.PdfReader(f)
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
        return text
    
def summarize(text):    
    response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Summarize this text:\n\n{text}"}

    ],
    max_tokens=200,
    temperature=0.7,
)
    response.choices[0].message.content





text = extract_text(PDF)

Answer = summarize(text)

print(Answer)




