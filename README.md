# Geospatial-Data-Validation-Tool

[![Python: 3.11](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)


## Overview

The Geospatial Data Validation Tool is designed to facilitate the validation and verification of geospatial datasets. This tool helps ensure the quality and consistency of geospatial data through various checks and validations. It supports common geospatial formats such as Shapefiles and GeoJSON.

## Features

1. **Topology Checks**
   - Detect overlapping polygons, gaps, or slivers.
   - Check for self-intersecting geometries.

2. **Coordinate System Validation**
   - Verify that datasets use consistent coordinate reference systems (CRS).
   - Offer automatic re-projection options.

3. **Data Completeness**
   - Identify missing attributes or incomplete records.
   - Validate attribute data types and value ranges.

4. **Error Reporting**
   - Generate detailed reports with visualizations of detected issues.
   - Provide recommendations for fixing errors.

5. **Input/Output Formats**
   - Support for common geospatial formats including Shapefiles, GeoJSON, and others.

## Installation

To install the tool, clone this repository and install the required dependencies using pip:

```bash
git clone https://github.com/yourusername/Geospatial-Data-Validation-Tool.git
cd Geospatial-Data-Validation-Tool

conda env create -f environment.yml
conda activate geovalidator

```

## Usage

### Load and Validate Geospatial Data

To load a GeoJSON file and perform validations, use the following script:

```python
import geopandas as gpd
from geovalidator.validators.topology import detect_overlaps, detect_gaps, detect_slivers, check_self_intersection

# Load the GeoJSON file
file_path = 'path/to/your/file.geojson'
gdf = gpd.read_file(file_path)

# Apply validation functions
overlapping_polygons = detect_overlaps(gdf)
gaps = detect_gaps(gdf)
slivers = detect_slivers(gdf, area_threshold=0.01)  # Adjust area_threshold as needed
self_intersections = check_self_intersection(gdf)

# Print results
print("Overlapping Polygons:")
print(overlapping_polygons)

print("\nGaps:")
print(gaps)

print("\nSlivers:")
print(slivers)

print("\nSelf-Intersecting Geometries:")
print(self_intersections)

```

## Contact

### Software Developer

- [Billy Ashmall](https://github.com/billyz313)



## License and Distribution

Geospatial-Data-Validation-Tool is distributed by BillyZ under the terms of the {type of license you choose} License. See
[LICENSE](LICENSE) in this directory for more information.

## Privacy & Terms of Use

Geospatial-Data-Validation-Tool abides to all of BillyZ's privacy and terms of use as described
at [https://ashmall.com/Privacy-Terms-of-Use.html](https://ashmall.com/Privacy-Terms-of-Use.html).
