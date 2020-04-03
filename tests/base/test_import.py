import bpy

def test_load_obj_box0():
    infile = "tests/base/src/box0.obj"
    bpy.ops.import_scene.obj(filepath=infile)
