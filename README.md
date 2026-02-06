# rag-linear-web-integrations

Packages RAG with provenance, Linear API sync, and an OpenAI-compatible web adapter with validation/sanity tooling.

## Purpose
Bundle practical integration layers needed for real deployments: retrieval, issue sync, and API compatibility.

## Features
- RAG pipeline with provenance-aware citations.
- Linear API synchronization for tasks and issue state.
- OpenAI-compatible adapter for UI/tool interoperability.
- Validation and sanity scripts for integration health checks.
- Environment-driven provider and integration toggles.

## Config
- `RAG_INDEX_PATH`: Local index/vector store location.
- `LINEAR_API_KEY`: API key for Linear sync.
- `LINEAR_TEAM_ID`: Target Linear team/workspace.
- `OPENAI_COMPAT_HOST`: Host for compatibility adapter.
- `ENABLE_WEB_ADAPTER`: Enable/disable web adapter startup.

## Quickstart
```bash
cp .env.example .env
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 axeon_web/adapter.py
```

## Roadmap
- Add bi-directional Linear sync conflict resolution.
- Add RAG ingestion pipelines for multiple source types.
- Add adapter auth middleware and rate limiting.
- Add end-to-end integration tests with fixtures.
