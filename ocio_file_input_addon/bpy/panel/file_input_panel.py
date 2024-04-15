import bpy

from bl_ui.properties_render import RenderButtonsPanel

from ocio_file_input_addon.bpy.operator.file_input_list_operator import FILEINPUTLIST_OT_entry_add, FILEINPUTLIST_OT_entry_move, FILEINPUTLIST_OT_entry_remove
from ocio_file_input_addon.bpy.operator.file_input_rule_operator import FILEINPURULE_OT_apply_on_scene


class RENDER_PT_file_input_panel(RenderButtonsPanel, bpy.types.Panel):

    bl_label = "File Input"
    bl_parent_id = "RENDER_PT_color_management"
    bl_options = {'DEFAULT_CLOSED'}

    COMPAT_ENGINES = {
        'BLENDER_RENDER',
        'BLENDER_EEVEE',
        'BLENDER_EEVEE_NEXT',
        'BLENDER_WORKBENCH',
    }

    def draw(self, context):
        layout = self.layout

        layout.label(text=" Rule Priority:")

        self._draw_file_input_list(context)

        self._draw_file_input_update(context)
    
    def _draw_file_input_update(self, context):
        file_input_list = context.scene.file_input_list
        file_input_list_index = context.scene.file_input_list_index
        if file_input_list_index < 0:
            return
    
        selected_rule = file_input_list[file_input_list_index]

        if not selected_rule:
            return

        layout = self.layout
        layout.separator()
        layout.label(text="Rule Condition:")
        layout.prop(selected_rule, "name", text="Name")
        layout.prop(selected_rule, "extension", text="Extension")
        layout.prop(selected_rule, "pattern", text="Pattern")
        layout.prop(selected_rule, "colorspace", text="Colorspace")

    def _draw_file_input_list(self, context):
        layout = self.layout.row()
        layout.template_list(
            "FILE_UL_file_input", "file_input_list",
            context.scene, "file_input_list",
            context.scene, "file_input_list_index"
        )
        col = layout.column()
        self._draw_add_remove_buttons(col, context)
        layout.separator()
        self._draw_move_buttons(col, context)

        self.layout.operator(FILEINPURULE_OT_apply_on_scene.bl_idname, text="Apply rules to Scene")
    
    def _draw_add_remove_buttons(self, layout, context):
        row = layout.row()
        row.operator(FILEINPUTLIST_OT_entry_add.bl_idname, text="", icon='ADD')
        
        row = layout.row()
        row.enabled = context.scene.file_input_list_index != len(context.scene.file_input_list) - 1
        row.operator(FILEINPUTLIST_OT_entry_remove.bl_idname, text="", icon='REMOVE')

    def _draw_move_buttons(self, layout, context):
        row = layout.row()
        row.enabled = self._move_up_is_enabled(context)
        props = row.operator(FILEINPUTLIST_OT_entry_move.bl_idname, text="", icon='TRIA_UP')
        props.direction = 'UP'

        row = layout.row()
        row.enabled = self._move_down_is_enabled(context)
        props = row.operator(FILEINPUTLIST_OT_entry_move.bl_idname, text="", icon='TRIA_DOWN')
        props.direction = 'DOWN'

    def _move_up_is_enabled(self, context):
        return 0 < context.scene.file_input_list_index < len(context.scene.file_input_list) - 1

    def _move_down_is_enabled(self, context):
        return context.scene.file_input_list_index < len(context.scene.file_input_list) - 2
