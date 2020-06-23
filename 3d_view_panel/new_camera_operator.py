import bpy


def main(context):
    camera_names = []

    for obj in bpy.context.scene.objects:
        if obj.type == 'CAMERA':
            camera_names.append(obj.name)

    if not camera_names:
        camera_name = bpy.context.scene.name + '_cam001'
        
        bpy.ops.object.camera_add()
        
        bpy.context.active_object.name = camera_name
        
        bpy.context.active_object.data.show_safe_areas = True

        bpy.context.active_object.data.passepartout_alpha = 0.95
    else:
        camera_names.sort(reverse=True)
        last_camera_number = int(camera_names[0][-3:])
        new_camera_number = last_camera_number + 1
        
        camera_name = bpy.context.scene.name + '_cam' + f'{new_camera_number:03}'
        
        bpy.ops.object.camera_add()
        
        bpy.context.active_object.name = camera_name
        
        bpy.context.active_object.data.show_safe_areas = True
        
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
