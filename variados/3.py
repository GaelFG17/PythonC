import nltk
nltk.download('punkt')

import tkinter as tk
from tkinter import scrolledtext
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def summarize_text():
    text = text_area.get("1.0", tk.END)
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, 2)  # Número de oraciones en el resumen
    result = "\n".join([str(sentence) for sentence in summary])
    result_area.delete("1.0", tk.END)
    result_area.insert(tk.END, result)

# Create the main window
root = tk.Tk()
root.title("Text Summarizer")

# Create a text area for input
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=15)
text_area.pack(padx=10, pady=10)

# Create a button to summarize the text
summarize_button = tk.Button(root, text="Summarize", command=summarize_text)
summarize_button.pack(pady=10)

# Create a text area for the result
result_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=15)
result_area.pack(padx=10, pady=10)

# Start the main loop
root.mainloop()