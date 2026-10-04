
from pathlib import Path

from src.ingestion.text_loader import load_text_file
from src.ingestion.text_chunker import chunk_text


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

    print("RAG Document Chunking Test")
    print("-" * 40)
    print(f"Source: {document['source']}")
    print(f"Document characters: {document['character_count']}")
    print(f"Total chunks: {len(chunks)}")

    for index, chunk in enumerate(chunks, start=1):
        print(f"\n--- Chunk {index} ({len(chunk)} characters) ---")
        print(chunk)


if __name__ == "__main__":
    main()
