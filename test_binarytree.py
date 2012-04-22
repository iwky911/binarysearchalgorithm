from vector import *
from binarytree import *

class TestBinaryTree:
    
    def setup(self):
        s = set(["bonjour", "hello", "gutentag", "ola", "bonjiourno"])
        self.tree = createNewBinaryTree(s)
    
    def test_inserted_elements_should_be_present(self):
        assert self.tree.search("bonjour") == "bonjour"
    
    def test_incorrect_queries_should_return_correct_answer(self):
        assert self.tree.search("gotentag") == "gutentag"
