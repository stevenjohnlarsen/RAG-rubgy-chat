from pypdf import PdfReader
import json

reader = PdfReader("./data/laws.pdf")
text = ""


pages = {
    "page_numbers":[],
    "page_content":[]
}

for index, page in enumerate(reader.pages):
    pages['page_content'].append(page.extract_text())
    pages['page_numbers'].append(index)

with open("data/pages.json", "w") as outfile: 
    json.dump(pages, outfile)