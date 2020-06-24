import bpy

def add_scene_strips(sc):
    """Adds sequencer strips for each camera in the given scene"""
    
    for obj in sc.objects:
            if obj.type == 'CAMERA':
                bpy.ops.sequencer.scene_strip_add(frame_start=bpy.context.scene.frame_start, scene=sc.name)
                bpy.context.scene.sequence_editor.active_strip.scene_camera = bpy.data.objects[obj.name]

def generate_strips(scene=None):
    """If a scene is provided, then it adds sequencer strips for that scene only.
       If no scene is provided, then it iterates over all scenes adding strips for
       each camera in every scene.
       
       scene must be of the blender scene type. You get the scene using
       bpy.data.scenes[SCENE_NAME]"""
    
    cur_scene = bpy.context.scene.name
    
    if scene:
        if not scene.name == cur_scene:
            add_scene_strips(scene)
    else:
        for sc in bpy.data.scenes:
            if not sc.name == cur_scene:
                add_scene_strips(sc)
        

area = bpy.context.area

cur_area = area.type

area.type = 'SEQUENCE_EDITOR'

generate_strips() # Call it with a scene, using bpy.data.scenes[SCENE_NAME], if you want to add strips for that scene only

area.type = cur_area

print("Finished adding scene strips!")

