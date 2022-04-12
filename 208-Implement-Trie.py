class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = False
        
class Trie:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for c in word:
            i = ord(c)-ord("a")
            if curr.children[i] == None:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.end = True
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        for c in word:
            i = ord(c)-ord("a")
            if curr.children[i] == None:
                return False
            curr = curr.children[i]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for c in prefix:
            i = ord(c)-ord("a")
            if curr.children[i] == None:
                return False
            curr = curr.children[i]
        return True
    
    
    
    
# Trie with dictionary




class TrieNode:
    def __init__(self, letter):
        self.children = {}
        self.isEnd = False


    
class Trie:
    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, words):
        node = self.root
        for letter in words:
            if letter not in node.children:
                node.children[letter] = TrieNode(letter)
            node = node.children[letter]

        node.isEnd = True

    
    def contains(self, words):
        node = self.root
        for letter in words:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return node.isEnd


    
    def startWith(self, word):
        node = self.root
        for letter in word:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return True



