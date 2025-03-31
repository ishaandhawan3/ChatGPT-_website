from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
import os

class ChatBot:
    def __init__(self):
        from config import DATABASE_DIR, DATA_PATH, EMBEDDING_MODEL
        
        self.embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)
        self.db = self._initialize_db(DATABASE_DIR, DATA_PATH)
        self.chat_history = []

    def _initialize_db(self, db_dir, data_path):
        if not os.path.exists(db_dir):
            os.makedirs(db_dir)
            raw_documents = []
            
            # Load all text files from data directory
            for file in os.listdir(data_path):
                if file.endswith(".txt"):
                    loader = TextLoader(os.path.join(data_path, file))
                    raw_documents.extend(loader.load())

            # Split and index documents
            text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            documents = text_splitter.split_documents(raw_documents)
            db = FAISS.from_documents(documents, self.embeddings)
            db.save_local(db_dir)
            return db
        else:
            return FAISS.load_local(db_dir, self.embeddings)

    def generate_response(self, query):
        # Retrieve relevant context
        docs = self.db.similarity_search(query, k=3)
        context = "\n".join([d.page_content for d in docs])
        
        # Generate response using local model
        from ollama import generate
        response = generate(
            model=MODEL_NAME,
            prompt=f"Context: {context}\n\nQuestion: {query}\nAnswer:",
            stream=False
        )
        
        self.chat_history.append((query, response))
        return response
