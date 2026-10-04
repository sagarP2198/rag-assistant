
from pathlib import Path

from src.ingestion.text_loader import load_text_file
from src.ingestion.text_chunker import chunk_text
from src.ingestion.metadata import create_chunk_records
from src.embeddings.embedding_generator import generate_embeddings
from src.embeddings.retriever import retrieve_relevant_chunks


def main():
    project_root = Path(__file__).resolve().parent

    document_path = (
        project_root
        / "data"
        / "raw"
        / "employee_leave_policy.txt"
    )

    document = load_text_file(str(document_path))

    chunks = chunk_text(
        document["text"],
        chunk_size=200,
        overlap=40,
    )

    records = create_chunk_records(
        document["source"],
        chunks,
    )

    texts = [record["text"] for record in records]
    vectors = generate_embeddings(texts)

    for record, vector in zip(records, vectors):
        record["embedding"] = vector

    question = "How many days of annual leave do employees receive?"

    results = retrieve_relevant_chunks(
        query=question,
        records=records,
        top_k=3,
    )

    print("\nRAG Semantic Search")
    print("=" * 50)
    print(f"Question: {question}")
    print(f"Results found: {len(results)}")

    for rank, result in enumerate(results, start=1):
        print(f"\n--- Result {rank} ---")
        print(f"Source: {result['source']}")
        print(f"Chunk ID: {result['chunk_id']}")
        print(f"Similarity score: {result['similarity_score']:.4f}")
        print(f"Text:\n{result['text']}")


if __name__ == "__main__":
    main()
