import os
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read() if os.path.exists("README.md") else ""

setup(
    name="atlas-morph",
    version="1.0.0",
    author="Medugu Wali, Mutmainnah Magaji, Ojo Timothy",
    author_email="m.wali@nileuniversity.edu.ng",
    description="Sovereign Diacritic-Aware Tokenization & Low-Rank Inference Acceleration Suite for N-ATLaS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/medugu-wali/atlas-morph",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Natural Language :: Yoruba",
        "Natural Language :: Hausa",
        "Natural Language :: Igbo",
        "Natural Language :: English",
    ],
    python_requires=">=3.9",
    install_requires=[
        # Core runtime has zero mandatory heavy dependencies
        # Standard library only for normalization and heuristic tokenization
    ],
    extras_require={
        "server": ["fastapi>=0.100.0", "uvicorn>=0.22.0", "pydantic>=2.0.0"],
        "hf": ["transformers>=4.40.0", "torch>=2.2.0"],
        "full": ["fastapi>=0.100.0", "uvicorn>=0.22.0", "pydantic>=2.0.0", "transformers>=4.40.0", "torch>=2.2.0"],
    },
    entry_points={
        "console_scripts": [
            "atlas-morph-server=atlas_morph.server:main",
        ],
    },
)
