from langchain_community.document_loaders import PyPDFLoader

book_iaf = PyPDFLoader("dados-texto.pdf")

# Lendo o arquivo que chamamos de Book Iaf

doc = book_iaf.load()

print(doc[15])



