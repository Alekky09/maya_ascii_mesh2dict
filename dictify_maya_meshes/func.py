
"""
Library made just to feed mesh data into python list of dictionaries.

Usage:
    from dictify_maya_meshes import func
    
    func.dictify_meshes('/example/path/to/file.ma')

"""
import re
import os

def dictify_meshes(maya_ascii):
    """
    Function that turns maya mesh data into a list of dicts.

    Args:
        maya_ascii (str): The path to maya ascii (.ma) file.

    Returns:
        A list of dictionaries of mesh objects. 
        Each dictionary contains the uid, name and position 
        of the mesh object.
    """

    if os.path.splitext(maya_ascii)[1] == ".ma":    # Check if the file is the correct type.
        try:                                        # Try to open the file.
            with open(maya_ascii) as f:
                list_of_results = []

                for line in f:
                    # If a mesh object is found.
                    if 'createNode mesh' in line:
                        mesh_dict = {}

                        # Store it's name.
                        name = re.search(r'(?<=")(.*?)(?=")', line)
                        mesh_dict['name'] = name.group()

                        # Check for it's position coordinates and store them if they exist.
                        if 'setAttr ".t" -type "double3"' in previous_line:
                            previous_line = previous_line[30:-2].split()
                            coords=(
                                float(previous_line[0]),
                                float(previous_line[1]),
                                float(previous_line[2]),
                            )
                            mesh_dict['position'] = coords
                        else:
                            mesh_dict['position'] = "Position not found!"
                        
                        # Grab the uid from the next line
                        nextline = f.next()
                        uid = re.search(r'(?<=")(.*?)(?=")', nextline)
                        mesh_dict['uid'] = uid.group()

                        # Append this mesh to the list of results
                        list_of_results.append(mesh_dict)
                        
                    # If mesh object is not found, store the line cause we
                    # might need it for position, in case the next line holds
                    # the mesh.
                    else:
                        previous_line = line

            return(list_of_results)
        
        except:
            return ("Error: Couldn't open the file.")
    else:
        return ("Error: Invalid file path.")