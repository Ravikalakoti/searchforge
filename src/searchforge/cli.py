"""
SearchForge CLI.
"""

import argparse

from .engine import SearchEngine


engine = SearchEngine()


def add_document(path: str):

    with open(
        path,
        "r",
        encoding="utf-8",
    ) as file:

        content = file.read()


    document_id = len(
        engine.documents
    ) + 1


    engine.add_document(
        document_id,
        content
    )


    engine.save()


    print(
        f"Document added: {document_id}"
    )



def search(query: str):

    engine.load()


    results = engine.search(
        query
    )


    for result in results:

        print(
            result.document_id,
            "|",
            result.score
        )



def stats():

    engine.load()


    print(
        "Popular searches:"
    )


    for query, count in engine.popular_queries():

        print(
            query,
            ":",
            count
        )



def main():

    parser = argparse.ArgumentParser(
        prog="searchforge"
    )


    subparsers = parser.add_subparsers(
        dest="command"
    )


    add_parser = subparsers.add_parser(
        "add"
    )

    add_parser.add_argument(
        "file"
    )


    search_parser = subparsers.add_parser(
        "search"
    )

    search_parser.add_argument(
        "query"
    )


    subparsers.add_parser(
        "stats"
    )


    args = parser.parse_args()


    if args.command == "add":

        add_document(
            args.file
        )


    elif args.command == "search":

        search(
            args.query
        )


    elif args.command == "stats":

        stats()



if __name__ == "__main__":

    main()
