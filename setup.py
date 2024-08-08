from setuptools import setup, find_packages

setup(
    name='poly-validator',
    version='0.1.0',
    description='GA tool for validating geospatial data with topology checks, coordinate system validation, and more.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='BillyZ',
    author_email='billyz313@gmail.com',
    url='https://github.com/billyz313/Geospatial-Data-Validation-Tool',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'geopandas',
        'shapely',
        'pyproj',
        'pyogrio',
        'fiona',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.11',
)
