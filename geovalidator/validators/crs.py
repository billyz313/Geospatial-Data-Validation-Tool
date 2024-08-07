import geopandas as gpd
from pyproj import CRS


def validate_crs(gdf: gpd.GeoDataFrame, expected_crs: str):
    """Validate that the GeoDataFrame has the expected CRS."""
    actual_crs = gdf.crs
    if actual_crs != expected_crs:
        raise ValueError(f"CRS mismatch: Expected {expected_crs}, found {actual_crs}")


def reproject_to_crs(gdf: gpd.GeoDataFrame, target_crs: str):
    """Reproject the GeoDataFrame to the target CRS."""
    return gdf.to_crs(target_crs)
