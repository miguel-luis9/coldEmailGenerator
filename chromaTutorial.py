import chromadb

client = chromadb.Client()
collection = client.create_collection(name="my_collection")

# collection.add(
#     documents=[
#         "This document is about New York",
#         "This document is about Delhi"
#     ],
#     ids = ['id1', "id2"]
# )

# all_docs = collection.get()
# print(all_docs)

# results = collection.query( # being 
#     query_texts=['Query is about India'],
#     n_results = 2
# )
# print(results)

# collection.delete(id=all_docs['ids'])
# collection.get()

collection.add(
    documents=[
        "This document is about New York",
        "This document is about Delhi"
    ],
    ids=["id3", "id4"],
    metadatas=[
        {"url": "https://en.wikipedia.org/wiki/New_York_City"},
        {"url": "https://en.wikipedia.org/wiki/New_Delhi"}
    ]
)

results = collection.query(
    query_texts=["query is abotu Chhloe Bhature"],
    n_results=2
)
print(results)