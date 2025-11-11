from setuptools import setup, find_packages

setup(
    name="fantasy-forge",
    version="0.1.0",
    description="A multifeatured application for fantasy fiction writers",
    author="Fantasy Forge Team",
    packages=find_packages(),
    install_requires=[
        "PyQt6>=6.6.1",
        "PyQt6-WebEngine>=6.6.0",
        "requests>=2.31.0",
        "nltk>=3.8.1",
        "spacy>=3.7.2",
        "Pillow>=10.1.0",
        "markdown>=3.5.1",
    ],
    entry_points={
        "console_scripts": [
            "fantasy-forge=fantasy_forge.main:main",
        ],
    },
    python_requires=">=3.10",
)
