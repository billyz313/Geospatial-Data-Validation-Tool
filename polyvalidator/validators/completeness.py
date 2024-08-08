import geopandas as gpd


def check_missing_attributes(gdf: gpd.GeoDataFrame, required_fields: list):
    """Check for missing attributes in the GeoDataFrame."""
    missing = [field for field in required_fields if field not in gdf.columns]
    return missing


def validate_attribute_types(gdf: gpd.GeoDataFrame, field_types: dict):
    """Validate that attributes have the expected data types."""
    for field, expected_type in field_types.items():
        if field in gdf.columns:
            if not gdf[field].map(lambda x: isinstance(x, expected_type)).all():
                raise TypeError(f"Field {field} does not match expected type {expected_type}")
