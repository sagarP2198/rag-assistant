
from pathlib import Path

from src.ingestion.text_loader import load_text_file


def main():
    project_root = Path(__file__).resolve().parent

    document_path = (
        project_root
        / "data"
        / "raw"
        / "employee_leave_policy.txt"
    )

    document = load_text_file(str(document_path))

    print("RAG Document Ingestion Test")
    print("-" * 40)
    print(f"Source: {document['source']}")
    print(f"Character count: {document['character_count']}")
    print("\nExtracted document text:\n")
    print(document["text"])


if __name__ == "__main__":
    main()
