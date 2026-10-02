# Agent Workflow Orchestrator

A checkpointed workflow API demonstrating plan/retrieve/act/verify orchestration with explicit run IDs and retry state.

## Run
```bash
pip install -e '.[dev]'
uvicorn app.main:app --reload
```

## Production extensions
Add durable workflow state, idempotency keys, async workers, retries/backoff, human approval nodes, event streams, and distributed locks.
