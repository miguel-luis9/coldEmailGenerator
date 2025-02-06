from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader

llm = ChatGroq(
    temperature=0,
    groq_api_key='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',
    model_name="llama-3.1-70b-versatile",
)
response = llm.invoke()
print(response.content)

loader = WebBaseLoader("https://careers.airbnb.com/positions/6492414/?gh_src=34ewj2")
page_data = loader.load().pop().page_content
print(page_data)