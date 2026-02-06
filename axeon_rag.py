from dataclasses import dataclass


@dataclass
class ProvenanceSnippet:
    text: str
    source: str


def retrieve_with_provenance(query: str) -> list[ProvenanceSnippet]:
    return [
        ProvenanceSnippet(text=f"Mock answer context for: {query}", source="local://demo-doc-1"),
    ]
