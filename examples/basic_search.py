from searchforge import SearchEngine


engine = SearchEngine()


engine.add_document(
    1,
    "Django is a powerful Python framework"
)

engine.add_document(
    2,
    "Python is used for machine learning"
)


results = engine.search(
    "python"
)


print(results)
