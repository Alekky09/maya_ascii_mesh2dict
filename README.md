# A library with a single function to read mesh objects from .ma maya files and return a list of dictionaries with mesh properties.
    * First run `python setup.py bdist_wheel`
    * Then `pip install ./dist/(whl_file_name)`
    * Usage in your py code:
    ```python
    from dictify_maya_meshes import func
    func.dictify_meshes('/path/to/example/file.ma')
    ```