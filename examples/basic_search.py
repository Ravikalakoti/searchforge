from searchforge import SearchEngine


engine = SearchEngine()

engine.add_document(
    1,
    "Django Python Developer"
)


results = engine.search(
    "python",
    limit=5
)


for result in results:
    print(result)