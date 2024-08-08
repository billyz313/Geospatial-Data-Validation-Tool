import geopandas as gpd
from shapely.geometry import Polygon
from shapely.validation import explain_validity


def detect_overlaps(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """Detect overlapping polygons in the GeoDataFrame."""
    overlaps = []

    # Iterate over each polygon
    for i, geom1 in enumerate(gdf.geometry):
        for j, geom2 in enumerate(gdf.geometry):
            # Skip if it's the same polygon
            if i >= j:
                continue
            # Check if polygons overlap
            if geom1.intersects(geom2):
                # Calculate the intersection (overlap) area
                intersection = geom1.intersection(geom2)
                if intersection.area > 0:
                    overlaps.append(intersection)

    # Create a GeoDataFrame for the overlaps
    overlap_gdf = gpd.GeoDataFrame(geometry=gpd.GeoSeries(overlaps), crs=gdf.crs)
    return overlap_gdf


def check_self_intersection(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """Check for self-intersections in the GeoDataFrame."""

    def has_self_intersection(geometry):
        # Use explain_validity to determine if there's a self-intersection
        validity = explain_validity(Polygon(geometry))
        return "Self-intersection" in validity

    # Create a boolean mask for self-intersecting polygons
    mask = gdf['geometry'].apply(has_self_intersection)
    # Return only the polygons that are self-intersecting
    intersecting = gdf[mask]
    return intersecting


def detect_gaps(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """Detect gaps between polygons in the GeoDataFrame."""
    # Create a single union geometry of all polygons
    union_geom = gdf.unary_union

    # Create bounding box
    bounding_box = union_geom.envelope

    # Calculate gaps as the difference between the bounding box and the union of geometries
    gaps = bounding_box.difference(union_geom)

    # If gaps are valid geometries, add them to the list
    if not gaps.is_empty:
        gap_gdf = gpd.GeoDataFrame(geometry=gpd.GeoSeries([gaps]), crs=gdf.crs)
        return gap_gdf
    else:
        return gpd.GeoDataFrame(geometry=gpd.GeoSeries([]), crs=gdf.crs)


def detect_slivers(gdf: gpd.GeoDataFrame, area_threshold: float) -> gpd.GeoDataFrame:
    """Detect sliver polygons in the GeoDataFrame."""
    slivers = []

    # Iterate over each polygon in the GeoDataFrame
    for geom in gdf.geometry:
        # Check if the polygon's area is below the threshold
        if geom.area < area_threshold:
            slivers.append(geom)

    # Create a GeoDataFrame for the slivers
    sliver_gdf = gpd.GeoDataFrame(geometry=gpd.GeoSeries(slivers), crs=gdf.crs)
    return sliver_gdf
