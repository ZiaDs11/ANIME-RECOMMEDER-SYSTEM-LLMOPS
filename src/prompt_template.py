from langchain_core.prompts import ChatPromptTemplate

def get_anime_prompt():
    system_prompt = (
        "You are an expert anime recommendation assistant. "
        "Use the following pieces of retrieved context to answer the question. "
        "If you don't know the answer, say that you don't know.\n\n"
        "Context:\n{context}"
    )
    
    # It must contain the precise {context} and {input} placeholders
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}"),
    ])
    return prompt