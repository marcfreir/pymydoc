# pymydoc
A minimalist way to document Python code in a GIT-like commit format.

> Status: ongoing (not released on PiPy, yet)

> Version: 0.0.0.1 (alpha)

# How to use it?

## Step 1: Install and Use the Library

Users can install it via `pip`:
```python
pip install pymydoc
```

or

```python
pip3 install pymydoc
```

To generate documentation from your Python script, you just need to include the following in your script:

Example: `project_example.py`

```python
import pymydoc

# Your code here
def print_hello_world():
    print("Hello World")

# Automatically generate documentation
pymydoc.pymydoc(__file__)

```

When you run `project_example.py`, the documentation will be automatically generated and saved as `documentation.md`.

With this setup, you can easily generate documentation by calling `auto_doc.auto_doc(...)` within your script. The library handles everything behind the scenes, creating a `documentation.md` file based on your code.

Ask me anything: marcfreir@outlook.com