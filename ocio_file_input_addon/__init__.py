

bl_info = {
    "name": "blender-ocio-file-input",
    "author": "Ni-g-3l",
    "version": (0, 1),
    "blender": (3, 5, 1),
    "location": "Render",
    "description": "Handle file input colorspace from OCIO Rules",
    "warning": "",
    "doc_url": "",
    "category": "Render",
}


def register():
    from ocio_file_input_addon.bpy.panel.file_input_panel import RENDER_PT_file_input_panel
    from ocio_file_input_addon.bpy.panel.file_input_list import FILE_UL_file_input
    from ocio_file_input_addon.bpy.operator.file_input_list_operator import FILEINPUTLIST_OT_entry_add, FILEINPUTLIST_OT_entry_remove, FILEINPUTLIST_OT_entry_move
    from ocio_file_input_addon.bpy.operator.file_input_rule_operator import FILEINPURULE_OT_apply_on_scene

    from bpy.utils import register_class
    register_class(FILEINPURULE_OT_apply_on_scene)
    register_class(FILEINPUTLIST_OT_entry_add)
    register_class(FILEINPUTLIST_OT_entry_remove)
    register_class(FILEINPUTLIST_OT_entry_move)
    register_class(FILE_UL_file_input)
    register_class(RENDER_PT_file_input_panel)

    from ocio_file_input_addon.bpy.property import register as register_properties
    register_properties()


def unregister():
    from ocio_file_input_addon.bpy.panel.file_input_panel import RENDER_PT_file_input_panel
    from ocio_file_input_addon.bpy.panel.file_input_list import FILE_UL_file_input
    from ocio_file_input_addon.bpy.operator.file_input_list_operator import FILEINPUTLIST_OT_entry_add, FILEINPUTLIST_OT_entry_remove, FILEINPUTLIST_OT_entry_move
    from ocio_file_input_addon.bpy.operator.file_input_rule_operator import FILEINPURULE_OT_apply_on_scene
    
    from bpy.utils import unregister_class
    unregister_class(FILEINPURULE_OT_apply_on_scene)
    unregister_class(FILEINPUTLIST_OT_entry_add)
    unregister_class(FILEINPUTLIST_OT_entry_remove)
    unregister_class(FILEINPUTLIST_OT_entry_move)
    unregister_class(FILE_UL_file_input)
    unregister_class(RENDER_PT_file_input_panel)

    from ocio_file_input_addon.bpy.property import unregister as unregister_properties
    unregister_properties()
