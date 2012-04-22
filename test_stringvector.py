from vector import  *

def test_vector_dist_should_be_the_edit_distance_between_two_vectors():
    v1 = "bonjour"
    v2 = "bonour"
    v3 = "bonghour"
    
    assert dist(v1, v1) == 0
    assert dist(v1, v2) == 1
    assert dist(v1, v3) == 2
