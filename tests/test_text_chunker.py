
import pytest

from src.ingestion.text_chunker import chunk_text


def test_empty_text_returns_no_chunks():
    assert chunk_text("") == []


def test_short_text_returns_one_chunk():
    assert chunk_text("Hello world", chunk_size=20, overlap=5) == [
        "Hello world"
    ]


def test_chunks_respect_maximum_size():
    text = "A" * 500

    chunks = chunk_text(text, chunk_size=100, overlap=20)

    assert len(chunks) > 1
    assert all(len(chunk) <= 100 for chunk in chunks)


def test_invalid_overlap_raises_error():
    with pytest.raises(ValueError):
        chunk_text("Hello world", chunk_size=10, overlap=10)
