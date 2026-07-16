"""
Autocomplete suggestion engine.
"""


class TrieNode:

    def __init__(self):

        self.children = {}

        self.is_end = False

        self.words = []



class SuggestionEngine:
    """
    Prefix based suggestion engine.
    """


    def __init__(self):

        self.root = TrieNode()



    def add(
        self,
        word: str,
    ) -> None:
        """
        Add word into trie.
        """

        node = self.root


        for char in word.lower():

            if char not in node.children:

                node.children[char] = TrieNode()


            node = node.children[char]


            if word not in node.words:

                node.words.append(word)



        node.is_end = True


    def suggest(
        self,
        prefix: str,
        limit: int = 5,
    ) -> list[str]:
        """
        Return suggestions for prefix.
        """

        node = self.root


        for char in prefix.lower():

            if char not in node.children:

                return []


            node = node.children[char]


        return node.words[:limit]
