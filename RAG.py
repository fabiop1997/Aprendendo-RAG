from langchain_community.document_loaders import PyPDFLoader

#from langchain_text_splitters import RecursiveCharacterTextSplitter


book_iaf = PyPDFLoader("dados-texto.pdf")

# Lendo o arquivo que chamamos de Book Iaf

doc = book_iaf.load()

print(doc[15])



