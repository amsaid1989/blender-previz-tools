import bpy


def main(context):
    camera_names = []

    # Find all cameras in the active scene and store their names
    for obj in bpy.context.scene.objects:
        if obj.type == 'CAMERA':
            camera_names.append(obj.name)

    if not camera_names:
        # If there are no cameras in the scene, then use the scene name followed by
        # '_cam001' as the new camera name
        camera_name = bpy.context.scene.name + '_cam001'
        
        # Create the new camera
        bpy.ops.object.camera_add()
        
        # Assign the camera name
        bpy.context.active_object.name = camera_name
        
        # Show the camera's safe areas
        bpy.context.active_object.data.show_safe_areas = True

        # Set the camera's passepartout
        bpy.context.active_object.data.passepartout_alpha = 0.95
    else:
        '''
        NOTE: The following assumes that you are only using the panel to create cameras.

        If you have created other cameras manually, things might not work as expected.
        '''

        # If there are cameras in the scene, then sort them in descending order
        camera_names.sort(reverse=True)

        # Get the last camera's number
        last_camera_number = int(camera_names[0][-3:])

        # Increment the camera number
        new_camera_number = last_camera_number + 1
        
        # Generate the new camera's name
        camera_name = bpy.context.scene.name + '_cam' + f'{new_camera_number:03}'
        
        # Create the camera
        bpy.ops.object.camera_add()
        
        # Assign the camera name
        bpy.context.active_object.name = camera_name
        
        # Show the camera's safe areas
        bpy.context.active_object.data.show_safe_areas = True
        
        # Set the camera's passepartout
        bpy.context.active_object.data.passepartout_alpha = 0.95
        

class NewPrevizCamera(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.new_previz_camera"
    bl_label = "New previz camera"

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'

    def execute(self, context):
        main(context)
        return {'FINISHED'}


def register():
    bpy.utils.register_class(NewPrevizCamera)


def unregister():
    bpy.utils.unregister_class(NewPrevizCamera)


if __name__ == "__main__":
    register()

    # test call
#    bpy.ops.object.simple_operator()
