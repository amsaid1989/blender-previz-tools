import bpy


class PrevizPanel(bpy.types.Panel):
    """Creates a Panel in the Viewport properties window"""
    bl_label = "Previz Tools Panel"
    bl_idname = "VIEW_PT_previz"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator("scene.new_previz_scene")
        
        row = layout.row()
        row.operator("object.new_previz_camera")

        cam_count = 0
        
        """ This makes sure that cameras that are not used in any scenes are
            not included in the count """
        for cam in bpy.data.cameras:
            if cam.users > 0:
                cam_count += 1
        
        row = layout.row()
        row.label(text="Total camera count: " + str(cam_count))


def register():
    bpy.utils.register_class(PrevizPanel)


def unregister():
    bpy.utils.unregister_class(PrevizPanel)


if __name__ == "__main__":
    register()
