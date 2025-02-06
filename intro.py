from langchain_groq import ChatGroq

llm = ChatGroq(
    model_name="llama-3.1-70b-versatile",
    temperature=0,
    groq_api_key="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"
)

response = llm.invoke("The first person to land on the moon was...")
print(response.content)