import bpy

area = bpy.context.area

cur_area = area.type

area.type = 'SEQUENCE_EDITOR'

cur_scene = bpy.context.scene.name

for sc in bpy.data.scenes:
    if not sc.name == cur_scene:
        for obj in sc.objects:
            if obj.type == 'CAMERA':
                bpy.ops.sequencer.scene_strip_add(frame_start=bpy.context.scene.frame_start, scene=sc.name)
                bpy.context.scene.sequence_editor.active_strip.scene_camera = bpy.data.objects[obj.name]

area.type = cur_area

print("Finished adding scene strips!")

