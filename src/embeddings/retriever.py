
from src.embeddings.embedding_generator import generate_embeddings


def retrieve_relevant_chunks(
    query: str,
    records: list[dict],
    top_k: int = 3,
) -> list[dict]:
    """Find the most relevant document chunks for a question."""

    if not query.strip():
        raise ValueError("Query must not be empty.")

    if top_k <= 0:
        raise ValueError("top_k must be greater than zero.")

    if not records:
        return []

    for record in records:
        if "embedding" not in record:
            raise ValueError(
                f"Missing embedding for chunk: "
                f"{record.get('chunk_id', 'unknown')}"
            )

    query_vector = generate_embeddings([query])[0]
    scored_records = []

    for record in records:
        chunk_vector = record["embedding"]

        if len(chunk_vector) != len(query_vector):
            raise ValueError(
                "Query and chunk embedding dimensions do not match."
            )

        score = sum(
            query_value * chunk_value
            for query_value, chunk_value in zip(
                query_vector, chunk_vector
            )
        )

        result = record.copy()
        result["similarity_score"] = float(score)
        scored_records.append(result)

    scored_records.sort(
        key=lambda item: item["similarity_score"],
        reverse=True,
    )

    return scored_records[:top_k]
