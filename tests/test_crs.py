import pytest
import geopandas as gpd
from shapely.geometry import Point
from polyvalidator.validators.crs import validate_crs, reproject_to_crs


def test_validate_crs():
    gdf = gpd.GeoDataFrame({
        'geometry': [Point(0, 0)]
    }, crs='EPSG:4326')  # CRS should be set here
    validate_crs(gdf, 'EPSG:4326')
    with pytest.raises(ValueError):
        validate_crs(gdf, 'EPSG:3857')


def test_reproject_to_crs():
    gdf = gpd.GeoDataFrame({
        'geometry': [Point(0, 0)],
    }, crs='EPSG:4326')
    gdf_reprojected = reproject_to_crs(gdf, 'EPSG:3857')
    assert gdf_reprojected.crs == 'EPSG:3857'
