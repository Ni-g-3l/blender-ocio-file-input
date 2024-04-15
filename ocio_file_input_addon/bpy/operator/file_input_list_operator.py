import bpy

class FILEINPUTLIST_OT_entry_add(bpy.types.Operator):
    """Add an entry to the file input list"""

    bl_idname = "fileinputlist.file_input_add"
    bl_label = "Add File Input Rule"

    def execute(self, context):
        file_input_list = context.scene.file_input_list

        new_rule = file_input_list.add()
        new_rule.name = "New rule"
        new_rule.extension = "*"
        new_rule.pattern = "*"
        new_rule.colorspace = "Non-Color"
        file_input_list.move(len(file_input_list) - 1, 0)
        context.scene.file_input_list_index = 0

        return {'FINISHED'}

class FILEINPUTLIST_OT_entry_remove(bpy.types.Operator):
    """Remove the selected entry from the file input list"""

    bl_idname = "fileinputlist.file_input_remove"
    bl_label = "Remove File Input Rule"

    def execute(self, context):
        file_input_list = context.scene.file_input_list
        active_index = context.scene.file_input_list_index

        file_input_list.remove(active_index)
        to_index = min(active_index, len(file_input_list) - 1)
        context.scene.file_input_list_index = to_index

        return {'FINISHED'}

class FILEINPUTLIST_OT_entry_move(bpy.types.Operator):
    """Move an file input rule in the list up or down"""

    bl_idname = "fileinputlist.file_input_move"
    bl_label = "Move File Input Rule"

    direction: bpy.props.EnumProperty(
        name="Direction",
        items=(
            ('UP', 'UP', 'UP'),
            ('DOWN', 'DOWN', 'DOWN'),
        ),
        default='UP',
    )

    def execute(self, context):
        file_input_list = context.scene.file_input_list
        active_index = context.scene.file_input_list_index

        delta = {
            'DOWN': 1,
            'UP': -1,
        }[self.direction]

        if active_index == 0 and delta == -1:
            return {'FINISHED'}
        
        if (active_index == len(file_input_list) - 1 or active_index == len(file_input_list) - 2) and delta == 1:
            return {'FINISHED'}

        to_index = (active_index + delta) % len(file_input_list)

        file_input_list.move(active_index, to_index)
        context.scene.file_input_list_index = to_index

        return {'FINISHED'}