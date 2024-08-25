from setuptools import setup, find_packages

setup(
    name="pymydoc",
    version="0.1.0",
    author="Marc Freir",
    author_email="marcfreir@outlook.com",
    description="A Python tool for auto-generating documentation from code.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/marcfreir/pymydoc",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: BSD 3-Clause License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['click'],
    entry_points={
        'console_scripts': [
            'pymydoc=utils.pymydoc:generate_documentation',  # Python API entry point
            'doc-cli=pymydoc.cli:cli',  # Click-based CLI entry point
        ],
    },
)
