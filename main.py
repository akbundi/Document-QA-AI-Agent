from ingest import extract_text_from_pdf
from search import BM25Retriever
from query_agent import query_ai
from arxiv_lookup import search_arxiv

def main():
    print("📄 Loading document...")
    file_path = "1570706159final.pdf"
    text = extract_text_from_pdf(file_path)
    docs = {file_path: text}
    retriever = BM25Retriever(docs)

    while True:
        print("\n🔍 Ask a question (or type 'exit'):")
        user_input = input(">> ").strip()

        if user_input.lower() == 'exit':
            break

        if user_input.startswith("lookup:"):
            description = user_input.replace("lookup:", "").strip()
            results = search_arxiv(description)
            for i, paper in enumerate(results, 1):
                print(f"\n{i}. {paper['title']}\nURL: {paper['pdf_url']}\nSummary: {paper['summary'][:300]}...\n")
            continue

        top_docs = retriever.retrieve(user_input)
        context = "\n\n---\n\n".join([f"From {name}:\n{text[:2000]}" for name, text, _ in top_docs])

        answer = query_ai(context, user_input)
        print(f"\n🤖 AI Answer:\n{answer}")

if __name__ == "__main__":
    main()