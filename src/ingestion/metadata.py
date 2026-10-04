
def create_chunk_records(source: str, chunks: list[str]) -> list[dict]:
    """Attach source information and an index to each text chunk."""

    records = []

    for index, chunk in enumerate(chunks, start=1):
        record = {
            "chunk_id": f"{source}_{index:03d}",
            "source": source,
            "chunk_index": index,
            "text": chunk,
            "character_count": len(chunk),
        }

        records.append(record)

    return records
