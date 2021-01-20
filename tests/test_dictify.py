from dictify_maya_meshes import func

def test_filetype():
    assert func.dictify_meshes("./example_file") == "Error: Invalid file path."

def test_validfile():
    assert func.dictify_meshes("./example_file.ma") == "Error: Couldn't open the file."

def test_example1():
    assert func.dictify_meshes("./example_files/example_file_1.ma") == [{'position': (1.0, 1.0, -6.0), 'name': 'SphereShape', 'uid': '94071E8E-4E72-008C-F8FD-62B8E4EF57DA'}, {'position': (-3.0, 2.0, 2.0), 'name': 'CubeShape', 'uid': '47C059BB-4D70-AC70-532B-38A9A7C92F68'}, {'position': (0.0, 0.0, 5.0), 'name': 'CylinderShape', 'uid': '9BC8DE79-468E-8469-0D05-C19729563BCC'}]

def test_example2():
    assert func.dictify_meshes("./example_files/example_file_2.ma") == [{'position': 'Position not found!', 'name': 'Sphere0Shape', 'uid': '5EF546F8-455A-8224-E6DB-FEB36AA9EDDB'}, {'position': (2.0, 0.0, 0.0), 'name': 'Sphere1Shape', 'uid': '6690914E-4E1B-DFD6-EB4A-2FB87D96806A'}, {'position': (4.0, 0.0, 0.0), 'name': 'Sphere2Shape', 'uid': '9A0827F9-4A4C-7FD7-0156-4A8F2B550C47'}, {'position': (6.0, 0.0, 0.0), 'name': 'Sphere3Shape', 'uid': 'EF8BFBB0-429D-DD24-6A55-81B5FA3811C7'}, {'position': (8.0, 0.0, 0.0), 'name': 'Sphere4Shape', 'uid': 'D9535AD9-46B5-86D0-A6F1-A19EAF9440E9'}, {'position': (10.0, 0.0, 0.0), 'name': 'Sphere5Shape', 'uid': '660AD31F-4BEC-8E41-E6DA-0CB40C5545D2'}, {'position': (0.0, 0.0, 5.0), 'name': 'CubeShape0', 'uid': '72070BAB-4B18-8FC4-6F38-C3963782402B'}, {'position': (2.0, 0.0, 5.0), 'name': 'CubeShape1', 'uid': '9DA5671B-479E-E41E-EC60-CBADB57A50EE'}, {'position': (4.0, 0.0, 5.0), 'name': 'CubeShape2', 'uid': '62D4BC4B-4A8F-ECF0-CFA4-2F8370F0253B'}, {'position': (6.0, 0.0, 5.0), 'name': 'CubeShape3', 'uid': '487F8F62-4AB3-BA1B-18D3-E587FBE33DBD'}, {'position': (8.0, 0.0, 5.0), 'name': 'CubeShape4', 'uid': '92351D98-4CC0-C4B7-5784-02872136E2D1'}, {'position': (10.0, 0.0, 5.0), 'name': 'CubeShape5', 'uid': '6AB47E23-46DC-3BE0-5FA6-5788661D3A9F'}]

def test_example3():
    assert func.dictify_meshes("./example_files/example_file_3.ma") == [{'position': (-9.724561399969902, 3.5468205018979577, -3.4691659115871456), 'name': 'TorusShape', 'uid': 'B9F64504-4669-159D-DE92-F597123DE5D5'}, {'position': (-4.2535554275807055, -2.8129398775047765, 3.7694855699836083), 'name': 'CubeShape', 'uid': 'E7714789-4F0C-4CCB-139C-BB8165401AB1'}, {'position': (7.738325659053141, 3.3811088323328273, -5.709179068123255), 'name': 'ConeShape', 'uid': '387F5B39-4F3E-4FE9-6636-AEBEC55AC369'}, {'position': 'Position not found!', 'name': 'SphereShape', 'uid': 'D6223292-4632-9F4E-25FE-38B2D04FB995'}]