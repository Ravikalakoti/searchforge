# SearchForge

A lightweight full-text search engine for Python.

SearchForge is a pure Python search library that provides fast document indexing, TF-IDF ranking, fuzzy search, autocomplete, metadata filtering, highlighted search results, persistent storage, and a simple command-line interface.

It is designed for developers who need an easy-to-integrate search engine for Python applications without external dependencies.

---

## Installation

Install SearchForge from PyPI:

```bash
pip install searchforge
```

Verify the installation:

```bash
searchforge --version
```

---

## Features

* Full-text document search
* Inverted index
* TF-IDF ranking
* Tokenization
* Text normalization
* Stop-word removal
* Fuzzy search
* Autocomplete suggestions
* Metadata filtering
* Highlighted search results
* Persistent document storage
* Persistent search index
* Search analytics
* Command-line interface

---

## Quick Start

```python
from searchforge import SearchEngine

engine = SearchEngine()

engine.add_document(
    1,
    "Python Django Developer"
)

engine.add_document(
    2,
    "FastAPI REST API Tutorial"
)

results = engine.search("python")

for result in results:
    print(result.document_id)
    print(result.score)
```

---

## CLI

Add a document

```bash
searchforge add sample.txt
```

Search

```bash
searchforge search "python"
```

View search analytics

```bash
searchforge stats
```

Display version

```bash
searchforge --version
```

---

## Basic Search

```python
results = engine.search("django")
```

Returns a ranked list of matching documents.

---

## Metadata Filtering

```python
engine.add_document(
    1,
    "Python Django Guide",
    metadata={
        "category": "Programming"
    }
)

results = engine.search(
    "python",
    filters={
        "category": "Programming"
    }
)
```

---

## Autocomplete

```python
engine.suggest("py")
```

Example output

```python
["python", "pytest"]
```

---

## Search Analytics

```python
engine.search("python")
engine.search("python")

print(engine.popular_queries())
```

Example

```python
[("python", 2)]
```

---

## Project Highlights

* Pure Python implementation
* No external search server required
* Easy to integrate into existing projects
* Suitable for small to medium-sized applications
* Published on PyPI
* Command-line support included

---

## Typical Use Cases

SearchForge can be used in:

* Django applications
* Flask applications
* FastAPI applications
* Documentation search
* Portfolio projects
* Knowledge base systems
* Blog search
* Product catalog search
* Local desktop applications
* Educational projects

---

## Requirements

* Python 3.10 or newer

---

## Source Code

GitHub

https://github.com/Ravikalakoti/searchforge

PyPI

https://pypi.org/project/searchforge/

Issue Tracker

https://github.com/Ravikalakoti/searchforge/issues

---

## License

MIT License

---

## Author

**Ravi Singh Kalakoti**

Python Backend Developer

GitHub:
https://github.com/Ravikalakoti

PyPI:
https://pypi.org/project/searchforge/
