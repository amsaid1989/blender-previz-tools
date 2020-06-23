import bpy
import os

tracks = []

for seq in bpy.context.scene.sequence_editor.sequences:
    tracks.append(seq.channel)
    seq.mute = True

tracks.sort(reverse=True)

path = bpy.context.scene.render.filepath

for i in tracks:
    for seq in bpy.context.scene.sequence_editor.sequences:
        if seq.channel == i:
            seq.mute = False
            scene_dir = seq.scene.name
            cam_dir = seq.scene_camera.name
            file = cam_dir + '_'
            bpy.context.scene.frame_start = seq.frame_final_start
            bpy.context.scene.frame_end = seq.frame_final_end - 1
            bpy.context.scene.render.filepath = os.path.abspath(os.path.join(path, scene_dir, cam_dir, file))
            # bpy.ops.render.render(animation=True) # Enable this if you want Cycles or EEVEE render
            bpy.ops.render.opengl(animation=True, sequencer=True) # This renders an opengl version from the sequencer
            seq.mute = True
            bpy.context.scene.render.filepath = path
            
print("RENDER COMPLETED SUCCESSFULLY!")
