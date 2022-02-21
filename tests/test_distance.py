# tests/test_distance
from mlproject.distance import haversine

def test_distance():
    assert round(haversine(2.38, 48.865070, 126.840806, 37.541530), 2) == 8959.36 
