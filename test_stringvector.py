from vector import Vector

def test_vector_dist_should_be_the_edit_distance_between_two_vectors():
    v1 = Vector("bonjour")
    v2 = Vector("bonour")
    v3 = Vector("bonghour")
    
    assert v1.dist(v1) == 0
    assert v1.dist(v2) == 1
    assert v1.dist(v3) == 2
