# Cold Email Generator 
An end-to-end Generative AI application designed to help Software and AI services companies efficiently generate personalized cold emails for outreach to potential clients. 
This project leverages open-source tools to build a powerful, customizable tool for automating cold email generation.

In this project I used a vector database, chromadb to add all the projects from the my_portfolio csv file. This database will act as a source to provide relevant projects to the inputted documents, providing
only the most relevant projects to each job based on the scraped data pulled from the document. 

I then created a chatGroq to prompt the llama-3.3-70b-versatile(the llm model I chose to use) to provide a JSON object based on the desired elements from the document, such as Role, Experience, Skills,
and Description(in this case). We then parse through the JSON object to validate we received the desired fields from the job prompt.

Then I used the output from the job prompt as input to write the email. This uses the job JSON object to identify relevant projects in the csv file and write the cold email accordingly with the related projects.

I then used streamlit to allow users to input job positions, to test out the cold email generator application.

## Technologies
- Llama 3.1: Open-source large language model (LLM) for generating high-quality email content.
- ChromaDB: Vector database for semantic search and efficient storage/retrieval of embeddings.
- Langchain: Framework for building LLM-based applications, handling prompt management, chaining tasks, and integrating external tools like vector stores.
- Streamlit: Frontend framework for building interactive web applications, allowing users to input preferences and generate emails with a user-friendly interface.

## Key Features
- AI-Powered Email Generation: Generates personalized and relevant cold emails using Llama 3.1.
- Semantic Search & Contextual Suggestions: Utilizes ChromaDB for intelligent context-based recommendations.
- Modular & Scalable Design: Easily extendable and adaptable to different industries or client types.
- User-Friendly Interface: Built with Streamlit for a smooth and intuitive user experience.

## Use Case
- Helps sales and business development teams at Software and AI services companies automate and streamline their outreach processes.
- Reduces manual effort while ensuring emails remain relevant, personalized, and engaging for potential clients.

This project is based on [End-to-End GenAI Project]{https://www.youtube.com/watch?v=CO4E_9V6li0&list=LL&index=1&t=1s}
