from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain_community.document_loaders import CSVLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="llama3-8b-8192",
    groq_api_key=os.environ["GROQ_API_KEY"],
)

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectordb_file_path = "faiss_index"

def create_vector_db():
    loader = CSVLoader(file_path="faqs.csv",source_column="prompt")
    data = loader.load()

    vectordb = FAISS.from_documents(documents = data, embedding = embeddings)

    vectordb.save_local(vectordb_file_path)


def get_qa_chain():
    vectordb = FAISS.load_local(vectordb_file_path,embeddings,allow_dangerous_deserialization=True)

    retriever = vectordb.as_retriever(score_threshold=0.5)

    prompt_template = """Given the following context and a question, generate an answer based on this context only.
    In the answer try to provide as much text as possible from "response" section in the source document context without making much changes.
    If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.

    CONTEXT: {context}

    QUESTION: {question}"""

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    chain = RetrievalQA.from_chain_type(llm=llm,
                                        chain_type="stuff",
                                        retriever=retriever,
                                        input_key="query",
                                        return_source_documents=True,
                                        chain_type_kwargs={"prompt": PROMPT})

    return chain

if __name__ == "__main__":
    create_vector_db()
    chain = get_qa_chain()
