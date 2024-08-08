import pytest
import geopandas as gpd
from shapely.geometry import Point
from polyvalidator.validators.completeness import check_missing_attributes, validate_attribute_types


def test_check_missing_attributes():
    gdf = gpd.GeoDataFrame({
        'geometry': [Point(0, 0)],
        'name': ['A']
    })
    missing = check_missing_attributes(gdf, ['name', 'id'])
    assert 'id' in missing


def test_validate_attribute_types():
    gdf = gpd.GeoDataFrame({
        'geometry': [Point(0, 0)],
        'value': [10]
    })
    validate_attribute_types(gdf, {'value': int})
    with pytest.raises(TypeError):
        validate_attribute_types(gdf, {'value': str})
