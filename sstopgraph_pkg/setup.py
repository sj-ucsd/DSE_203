from setuptools import setup, find_packages

setup(
    name='sstopgraph-pkg',
    version='1.1.2',
    author='Sagar Jogadhenu, Laben Fisher, Prakhar Shukla',
    description='Package to convert semistructred \
                 (json) data to property graph',
    packages=find_packages(),
    install_requires=[
    "jsonpath_ng"
    ],
)
