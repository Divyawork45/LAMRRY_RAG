
import os
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Weaviate
import weaviate
from weaviate.embedded import EmbeddedOptions
from langchain.text_splitter import CharacterTextSplitter
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser


def get_response(msg, prev=None):
    os.environ["OPENAI_API_KEY"] = '' #api key 
    current_directory = os.path.dirname(os.path.abspath(__file__))
    data = os.path.join(current_directory, 'mcq.txt')
    loader = TextLoader(data)
    documents = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_documents(documents)

    client = weaviate.Client(
      embedded_options = EmbeddedOptions()
    )

    vectorstore = Weaviate.from_documents(
        client = client,    
        documents = chunks,
        embedding = OpenAIEmbeddings(),
        by_text = False,
    )

    retriever = vectorstore.as_retriever()


    template = """You are an assistant for question-answering tasks. 
    Use the following pieces of retrieved context to answer the question. 
    If you don't know the answer, just say that you don't know. 
    Use three sentences maximum and keep the answer concise.
    Question: {question} 
    Context: {context} 
    Answer:
    """
    prompt = ChatPromptTemplate.from_template(template)



    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

    rag_chain = (
        {"context": retriever,  "question": RunnablePassthrough()} 
        | prompt 
        | llm
        | StrOutputParser() 
    )

    query = msg
    resp = rag_chain.invoke(query)
    return resp

