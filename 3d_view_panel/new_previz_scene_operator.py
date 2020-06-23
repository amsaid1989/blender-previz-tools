import bpy


def main(context):
    scene_names = []

    for sc in bpy.data.scenes:
        scene_names.append(sc.name)

    scene_names.sort(reverse=True)

    last_scene_number = int(scene_names[0].split('_')[1])

    new_scene_number = last_scene_number + 10

    new_scene_name = 'sc_' + f'{new_scene_number:04}' # Converts the scene number into string and pads it with zeroes

    bpy.ops.scene.new(type='EMPTY')

    bpy.context.scene.name = new_scene_name

    area = bpy.context.area

    cur_ar_type = area.type

    area.type = 'OUTLINER'

    bpy.ops.outliner.collection_new()
    bpy.ops.outliner.collection_new()

    bpy.context.scene.collection.children[0].name = new_scene_name + '_objects'
    bpy.context.scene.collection.children[1].name = new_scene_name + '_cameras'
    
    bpy.context.scene.safe_areas.title[0] = 0
    bpy.context.scene.safe_areas.title[1] = 0
    
    bpy.context.scene.safe_areas.action[0] = 1 - (1920 / 2048)
    bpy.context.scene.safe_areas.action[1] = 1 - (800 /1080)

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
