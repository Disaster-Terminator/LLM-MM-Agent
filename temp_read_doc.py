import os
import win32com.client
from pathlib import Path

doc_path = r"G:\Math Modeling\B题\B题 大型展销会临时工招聘与排班优化问题.doc"
output_path = r"G:\Math Modeling\LLM-MM-Agent\temp_read_doc.txt"

# Open Word
word = win32com.client.Dispatch("Word.Application")
word.Visible = False

# Open the document
doc = word.Documents.Open(doc_path)
text = doc.Content.Text

with open(output_path, "w", encoding="utf-8") as f:
    f.write(text)

doc.Close()
word.Quit()
print("Done")