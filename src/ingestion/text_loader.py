
from pathlib import Path


def load_text_file(file_path: str) -> dict:
    """Read a UTF-8 text file and return its content and metadata."""

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Document not found: {path}")

    if not path.is_file():
        raise ValueError(f"Expected a file, not a directory: {path}")

    text = path.read_text(encoding="utf-8").strip()

    if not text:
        raise ValueError(f"Document is empty: {path}")

    return {
        "source": path.name,
        "text": text,
        "character_count": len(text),
    }
