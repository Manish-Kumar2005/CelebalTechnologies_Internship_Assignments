import pandas as pd
import faiss
import os
import numpy as np
from sentence_transformers import SentenceTransformer
from transformers import pipeline

# Load dataset
df = pd.read_csv("Training Dataset.csv")
df.fillna("Unknown", inplace=True)

# Step 1: Convert rows to text documents
def row_to_text(row):
    return f"Applicant {row['Loan_ID']} is a {row['Gender']} {row['Married']} applicant with {row['Education']} education, {row['Self_Employed']} self-employed, income of {row['ApplicantIncome']} and co-applicant income of {row['CoapplicantIncome']}. Loan amount: {row['LoanAmount']}, Term: {row['Loan_Amount_Term']}, Credit history: {row['Credit_History']}, Property area: {row['Property_Area']}. Loan status: {row['Loan_Status']}."

documents = df.apply(row_to_text, axis=1).tolist()

# Step 2: Generate embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(documents, show_progress_bar=True)

# Step 3: Store in FAISS index
d = embeddings[0].shape[0]
index = faiss.IndexFlatL2(d)
index.add(np.array(embeddings))

# Step 4: Question Answering pipeline
qa_model = pipeline("text2text-generation", model="google/flan-t5-base")

# Step 5: QA loop
def rag_chatbot():
    print("\n Loan Prediction RAG Chatbot. Type 'exit' to quit.")
    while True:
        query = input("\nYou: ")
        if query.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        
        query_embedding = model.encode([query])
        D, I = index.search(np.array(query_embedding), k=3)
        context = "\n".join([documents[i] for i in I[0]])
        prompt = f"Context: {context}\n\nQuestion: {query}\nAnswer:"

        #Use max_new_tokens to avoid warning
        response = qa_model(prompt, max_new_tokens=256, do_sample=False)[0]['generated_text']
        print(f"\n: {response}")

if __name__ == "__main__":
    rag_chatbot()
