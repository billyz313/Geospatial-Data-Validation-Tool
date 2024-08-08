import geopandas as gpd
from shapely.geometry import Polygon

from polyvalidator.validators.topology import detect_overlaps, check_self_intersection, detect_gaps, detect_slivers


def test_detect_overlaps():
    # Create a GeoDataFrame with overlapping polygons
    gdf = gpd.GeoDataFrame({
        'geometry': [
            Polygon([(0, 0), (2, 0), (2, 2), (0, 2)]),  # Polygon 1
            Polygon([(1, 1), (3, 1), (3, 3), (1, 3)]),  # Polygon 2 - Overlaps with Polygon 1
            Polygon([(3, 3), (4, 3), (4, 4), (3, 4)])  # Polygon 3
        ]
    })

    overlaps = detect_overlaps(gdf)

    # Assert there is one overlap
    assert len(overlaps) == 1
    # Check if the overlap polygon has correct geometry
    expected_overlap = Polygon([(1, 1), (2, 1), (2, 2), (1, 2)])
    assert overlaps.iloc[0].geometry.equals(expected_overlap)


def test_check_self_intersection():
    gdf = gpd.GeoDataFrame({
        'geometry': [
            Polygon([(0, 0), (1, 0), (1, 1), (0, 1)]),  # Valid Polygon
            Polygon([(0, 0), (1, 1), (0, 1), (1, 0)]),  # Self-intersecting Polygon
            Polygon([(2, 2), (3, 2), (3, 3), (2, 3)])  # Valid Polygon
        ]
    })

    intersecting = check_self_intersection(gdf)
    print(intersecting)  # Debug print to check which polygons are identified
    assert len(intersecting) == 1  # Expecting one self-intersecting polygon


def test_detect_gaps():
    # Create a GeoDataFrame with intentional gaps
    gdf = gpd.GeoDataFrame({
        'geometry': [
            Polygon([(0, 0), (2, 0), (2, 2), (0, 2)]),  # Polygon 1
            Polygon([(3, 0), (5, 0), (5, 2), (3, 2)])  # Polygon 2 - Leaves a gap between polygons
        ]
    })

    gaps = detect_gaps(gdf)

    # Assert there is one gap
    assert len(gaps) == 1
    # Check if the gap polygon has correct geometry
    expected_gap = Polygon([(2, 0), (3, 0), (3, 2), (2, 2)])
    assert gaps.iloc[0].geometry.equals(expected_gap)


def test_detect_slivers():
    # Create a GeoDataFrame with a sliver polygon
    gdf = gpd.GeoDataFrame({
        'geometry': [
            Polygon([(0, 0), (2, 0), (2, 2), (0, 2)]),  # Polygon 1 (area: 4)
            Polygon([(2, 2), (2.05, 2), (2.05, 2.05), (2, 2.05)]),  # Sliver polygon (area: 0.0025)
            Polygon([(3, 3), (4, 3), (4, 4), (3, 4)])  # Polygon 3 (area: 1)
        ]
    })

    # Use a smaller area threshold
    slivers = detect_slivers(gdf, area_threshold=0.01)

    # Assert there is one sliver
    assert len(slivers) == 1
    # Check if the sliver polygon has correct geometry
    expected_sliver = Polygon([(2, 2), (2.05, 2), (2.05, 2.05), (2, 2.05)])
    assert slivers.iloc[0].geometry.equals(expected_sliver)
