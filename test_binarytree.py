from vector import *
from binarytree import *

class TestBinaryTree:
    
    def setup(self):
        s = set(map(lambda x: Vector(x) ,["bonjour", "hello", "gutentag", "ola"]))
        self.tree = createNewBinaryTree(Vector("bonjiourno"),s)
    
    def test_inserted_elements_should_be_present(self):
        assert self.tree.search(Vector("bonjour")).values == "bonjour"
    
    def test_incorrect_queries_should_return_correct_answer(self):
        assert self.tree.search(Vector("gotentag")).values == "gutentag"
