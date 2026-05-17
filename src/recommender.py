from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_groq import ChatGroq
from src.prompt_template import get_anime_prompt

class AnimeRecommender:
    def __init__(self, retriever, api_key: str, model_name: str):
        # 1. Initialize the ChatGroq LLM
        self.llm = ChatGroq(api_key=api_key, model=model_name, temperature=0)
        
        # 2. Grab your custom prompt template
        self.prompt = get_anime_prompt()

        # 3. Create the document chain (formats the context + prompt + LLM)
        # This completely replaces the old chain_type="stuff" configuration
        document_chain = create_stuff_documents_chain(self.llm, self.prompt)

        # 4. Create the final modern retrieval chain
        self.rag_chain = create_retrieval_chain(retriever, document_chain)

    def get_recommendation(self, query: str):
        # 5. Invoke the modern chain. 
        # Modern chains expect the input key to be "input" rather than "query"
        result = self.rag_chain.invoke({"input": query})
        
        # Modern retrieval chains return a dictionary where the text answer is under 'answer'
        return result['answer']