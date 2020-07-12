import bpy
import os

tracks = []

# Go over the strips and keep note of what track each of them is located at
for seq in bpy.context.scene.sequence_editor.sequences:
    tracks.append(seq.channel)
    
    # Disable the strip
    seq.mute = True

# Sort the tracks in descending order
tracks.sort(reverse=True)

'''
Create a variable that stores the render filepath defined in the scene settings.

The render filepath defined in the scene settings should be a directory where you will
render all your scenes.

The directories for each scene and its cameras will be created automatically.
'''
path = bpy.context.scene.render.filepath

for i in tracks:
    for seq in bpy.context.scene.sequence_editor.sequences:
        if seq.channel == i:
            # Find the strip that exists on the track and render it

            # Re-enable the strip
            seq.mute = False

            # Define the scene render folder based on the strip's scene name
            scene_dir = seq.scene.name

            # Define the strip's render folder based on the strip's camera name
            cam_dir = seq.scene_camera.name

            # Define the render filename
            # (assumes an image sequence will be rendered so adds an underscore to separate the
            # filename from the frame numbers)
            filename = cam_dir + '_'

            # Sets the render start frame based on the strip's start frame
            bpy.context.scene.frame_start = seq.frame_final_start

            # Sets the render end frame based on the strip's end frame
            bpy.context.scene.frame_end = seq.frame_final_end - 1

            # Sets the final render path using the render settings path, scene directory,
            # camera directory and filename
            bpy.context.scene.render.filepath = os.path.abspath(os.path.join(path, scene_dir, cam_dir, filename))

            # Render
            # bpy.ops.render.render(animation=True) # Enable this if you want Cycles or EEVEE render
            bpy.ops.render.opengl(animation=True, sequencer=True) # This renders an opengl version from the sequencer

            # Disable the scene strip again
            seq.mute = True

            # Reset the scene's render filepath in the render settings
            bpy.context.scene.render.filepath = path
            
print("RENDER COMPLETED SUCCESSFULLY!")
