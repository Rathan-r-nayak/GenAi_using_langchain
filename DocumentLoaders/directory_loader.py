from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader = DirectoryLoader(
    path="data",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()

with open("data/contet.txt", "w") as f:
    for i in docs:
        f.write("page : "+i.metadata['page_label']+"\n")
        f.write(i.page_content.encode("utf-8", "ignore").decode("utf-8"))
        f.write("\n----------------------------------------------------------------------------------------\n")