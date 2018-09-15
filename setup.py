import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="parquet-metadata",
    version="0.0.1",
    author="Colin Dellow",
    author_email="cldellow@cldellow.com",
    description="A tool to show metadata about a Parquet file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cldellow/parquet-metadata",
    packages=setuptools.find_packages(),
    entry_points = {
        "console_scripts": ['parquet-metadata = parquet_metadata.parquet_metadata:main']
    },
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ),
)

