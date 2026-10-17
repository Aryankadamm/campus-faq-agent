# Campus FAQ Agent

A source-aware student support assistant. It retrieves the closest answer from a small campus guide, shows the source and match score, and hands off when the guide does not contain an answer.

## Run it

Requires Python 3.10+; no packages or API key required.

```bash
python agent.py
```

Try: `How can I get a replacement student card?` or `Can you tell me the cafeteria menu?` The first should cite the student services handbook; the second should hand off instead of inventing an answer.

## How it works

The demo uses transparent keyword overlap to retrieve an answer. This makes the retrieval and fallback behavior easy to inspect. In a production version, replace `retrieve()` with embeddings and a vector store, add a maintained knowledge source, and evaluate retrieval quality against a held-out question set. It is a small retrieval-agent prototype, not a production chatbot.

## Skills demonstrated

Python, information retrieval, grounding, source attribution, confidence thresholds, and safe fallback design.

