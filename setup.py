from setuptools import setup, find_packages

setup(
    name='geovalidator',
    version='0.1.0',
    description='Geospatial Data Validation Tool',
    author='BillyZ',
    author_email='billyz313@gmail.com',
    packages=find_packages(),
    install_requires=[
        'geopandas',
        'shapely',
        'pyproj',
        'fiona',
    ],
)
