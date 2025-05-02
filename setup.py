# run pip install -e . to install locally defined dependencies
from setuptools import setup, find_packages

setup(
    name="ml_packages",
    version="0.1.0",
    packages=find_packages(),  # This finds all packages with __init__.py files
    install_requires=[
        "pytest",
        "torch",
        "numpy",
        "convokit",
        "sentence_transformers",
        "umap-learn",
        "seaborn"
    ],
)
