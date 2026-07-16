# SearchForge

A lightweight full-text search engine built in Python.

SearchForge provides fast document indexing, ranking, fuzzy search, autocomplete, highlighting, metadata filtering, persistent storage, and a command-line interface.

## Installation

### Install from PyPI (Recommended)

```bash
pip install searchforge
```

### Install from Source

```bash
git clone https://github.com/<your-github-username>/searchforge.git
cd searchforge
pip install -e .
```

## PyPI

https://pypi.org/project/searchforge/

## Features

- Full-text search
- Inverted index based indexing
- TF-IDF ranking
- Tokenization and normalization
- Stop word removal
- Fuzzy search
- Autocomplete suggestions
- Metadata filtering
- Highlighted search results
- Persistent document storage
- Persistent search index
- Search analytics
- Command Line Interface (CLI)

## CLI Usage

### Add a document

```bash
searchforge add sample.txt
```

### Search documents

```bash
searchforge search "python"
```

### View search analytics

```bash
searchforge stats
```

### Show version

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

results = engine.search("python")

for result in results:
    print(result.document_id)
    print(result.score)
```

## Project Architecture

```text
SearchForge
│
├── Tokenizer
├── Normalizer
├── Stop Words
├── Inverted Index
├── Query Processor
├── Ranking Engine
│   └── TF-IDF
├── Storage
├── Analytics
├── CLI
└── Search Engine
```

## Development

Clone the repository:

```bash
git clone https://github.com/<your-github-username>/searchforge.git
cd searchforge
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment:

**macOS/Linux**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -e .
```

Run tests:

```bash
pytest
```

Build the package:

```bash
python -m build
```

Publish to PyPI:

```bash
twine upload dist/*
```

## Requirements

- Python 3.10+

## License

MIT License.

## Author

**Ravi Singh Kalakoti**

- GitHub: https://github.com/Ravikalakoti
- PyPI: https://pypi.org/project/searchforge/