import openai
import os
from langchain.chains import RetrievalQA
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import WebBaseLoader

# Ensure OpenAI API key is set
openai.api_key = os.getenv("OPENAI_API_KEY")

# Load Documentation URLs
doc_urls = [
    "https://segment.com/docs/",
    "https://docs.mparticle.com/",
    "https://docs.lytics.com/",
    "https://docs.zeotap.com/home/en-us/"
]

# Load and Process Documents
def load_docs(urls):
    documents = []
    for url in urls:
        try:
            loader = WebBaseLoader(url)
            docs = loader.load()
            documents.extend(docs)
        except Exception as e:
            print(f"Error loading {url}: {e}")
    return documents

documents = load_docs(doc_urls)

# Check if documents are loaded before proceeding
if not documents:
    print("No documents loaded. Please check the documentation URLs.")
    exit()

# Embed and Store Documents
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(documents, embeddings)

# Build the Chatbot Chain
qa_chain = RetrievalQA.from_chain_type(
    llm=openai.ChatCompletion.create,
    retriever=vectorstore.as_retriever(),
    return_source_documents=True
)

def chatbot():
    print("CDP Chatbot: Ask me anything about Segment, mParticle, Lytics, or Zeotap!")
    while True:
        query = input("You: ")
        if query.lower() in ['exit', 'quit', 'bye']:
            print("Goodbye!")
            break
        
        # Handle irrelevant questions
        irrelevant_keywords = ["movie", "weather", "sports", "news", "celebrity"]
        if any(keyword in query.lower() for keyword in irrelevant_keywords):
            print("Chatbot: I'm here to answer questions about Segment, mParticle, Lytics, or Zeotap.")
            continue
        
        # Example questions
        example_questions = {
            "how do i set up a new source in segment?": "To set up a new source in Segment, go to the Segment dashboard, navigate to 'Sources', click 'Add Source', choose the desired source type, and follow the setup instructions.",
            "how can i create a user profile in mparticle?": "In mParticle, user profiles are created automatically when user data is ingested. You can enrich profiles by sending user attributes via the mParticle API.",
            "how do i build an audience segment in lytics?": "To build an audience segment in Lytics, go to the Lytics dashboard, click on 'Audiences', then 'Create New Audience', and define rules based on user behavior.",
            "how can i integrate my data with zeotap?": "To integrate data with Zeotap, use the Zeotap API or upload CSV files via the Zeotap dashboard under the 'Data Integration' section."
        }
        
        if "compare" in query.lower() or "difference" in query.lower():
            response = "Each CDP has its own unique approach. Segment focuses on event tracking and integrations, mParticle provides real-time data orchestration, Lytics emphasizes audience intelligence, and Zeotap specializes in deterministic identity resolution. For specific comparisons, please specify the features you're interested in."
        elif "advanced" in query.lower() or "complex" in query.lower():
            response = "For advanced configurations, integrations, or specific use cases, refer to the official documentation or specify the exact scenario. Example: 'How do I set up real-time event forwarding in mParticle?'"
        elif query.lower() in example_questions:
            response = example_questions[query.lower()]
        else:
            try:
                result = qa_chain(query)
                response = result["result"]
                sources = result["source_documents"]
                if sources:
                    response += "\n\nSource(s): " + ", ".join([doc.metadata.get("source", "Unknown") for doc in sources])
            except Exception as e:
                response = f"Error processing request: {e}"
        
        print("Chatbot:", response)

if __name__ == "__main__":
    chatbot()
