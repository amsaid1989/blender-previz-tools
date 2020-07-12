import bpy


def main(context):
    scene_names = []

    # Gather all the scenes in the file and store their names
    for sc in bpy.data.scenes:
        scene_names.append(sc.name)

    # Sort the scene names alphabetically
    scene_names.sort(reverse=True)

    '''
    Split the scene name at the underscore (based on the naming convention) and find
    the last scene number
    '''
    last_scene_number = int(scene_names[0].split('_')[1])

    # Increment the scene number
    new_scene_number = last_scene_number + 10

    new_scene_name = 'sc_' + f'{new_scene_number:04}' # Converts the scene number into string and pads it with zeroes

    # Create a new scene using the settings of the active scene
    bpy.ops.scene.new(type='EMPTY')

    # Assign the new scene name
    bpy.context.scene.name = new_scene_name

    # Store the current area type and change it to the outliner
    area = bpy.context.area
    cur_ar_type = area.type
    area.type = 'OUTLINER'

    # Create two new collections in the scene
    bpy.ops.outliner.collection_new()
    bpy.ops.outliner.collection_new()

    '''
    Rename the scene collections using the scene name as a prefix.
    
    The collections need to have the scene name as a prefix, because Blender stores all
    collection in the file in one place, so you can't have two collections with the same
    name.
    '''
    bpy.context.scene.collection.children[0].name = new_scene_name + '_objects'
    bpy.context.scene.collection.children[1].name = new_scene_name + '_cameras'
    
    '''
    The following 4 lines of code define the safe area overlay in the camera.

    While working on the previz, I was using scene resolution that is larger than the
    final resolution I was rendering at to have a bit of an overscan in case I wanted
    to tweak the shot's framing in the edit.

    Therefore, I needed to use the safe area overlay to show the actual resolution I will
    use when rendering from my editing program so I can use them as a guide when setting up
    the cameras in Blender.

    These settings define the safe areas based on the resolution of my project, so you will
    need to tweak them to fit yours.
    '''
    bpy.context.scene.safe_areas.title[0] = 0
    bpy.context.scene.safe_areas.title[1] = 0
    
    bpy.context.scene.safe_areas.action[0] = 1 - (1920 / 2048)
    bpy.context.scene.safe_areas.action[1] = 1 - (800 /1080)

    # Make the current area a 3D view
    area.type = 'VIEW_3D'


class NewPrevizScene(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "scene.new_previz_scene"
    bl_label = "New previz scene"

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'

    def execute(self, context):
        main(context)
        return {'FINISHED'}


def register():
    bpy.utils.register_class(NewPrevizScene)


def unregister():
    bpy.utils.unregister_class(NewPrevizScene)


if __name__ == "__main__":
    register()

    # test call
#    bpy.ops.object.simple_operator()
