from langchain_community.document_loaders import CSVLoader

loader = CSVLoader("data/NetworkHospitalList.csv")

docs = loader.load()
print(type(docs))

print(docs[0].metadata)

print(docs[0].page_content)