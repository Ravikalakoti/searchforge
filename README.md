````md
# SearchForge

A lightweight full-text search engine built in Python.

SearchForge provides fast document indexing, ranking, fuzzy search, autocomplete, highlighting, filtering and persistent storage.

## Features

- Full-text search
- Inverted index based indexing
- TF-IDF and BM25 ranking
- Tokenization and normalization
- Stop word removal
- Fuzzy search
- Autocomplete suggestions
- Metadata filtering
- Highlighted search results
- Persistent document storage
- Persistent index storage
- Search analytics
- Command line interface (CLI)

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd searchforge
````

Install:

```bash
pip install -e .
```

## CLI Usage

Add a document:

```bash
searchforge add sample.txt
```

Search:

```bash
searchforge search "python"
```

View analytics:

```bash
searchforge stats
```

Check version:

```bash
searchforge --version
```

## Python Usage

```python
from searchforge import SearchEngine


engine = SearchEngine()


engine.add_document(
    1,
    "Python Django Developer"
)


results = engine.search(
    "python"
)


for result in results:
    print(result.document_id, result.score)
```

## Architecture

```
SearchForge

├── Tokenizer
├── Normalizer
├── Stop Words
├── Inverted Index
├── Query Processor
├── Ranking Engine
│      ├── TF-IDF
│      └── BM25
├── Storage
├── CLI
└── Analytics
```

## Development

Run tests:

```bash
pytest
```

## License

MIT License

````