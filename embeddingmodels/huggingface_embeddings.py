from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

texts  = ["hello,how r u?","what r u doing?"]

vector = embedding.embed_documents(texts)
print(vector)