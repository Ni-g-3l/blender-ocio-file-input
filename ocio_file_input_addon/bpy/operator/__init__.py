def register_operators():
    from bpy.utils import register_class

    from ocio_file_input_addon.bpy.operator.file_input_list_operator import (
        FILEINPUTLIST_OT_entry_add, FILEINPUTLIST_OT_entry_remove,
        FILEINPUTLIST_OT_entry_move
    )

    from ocio_file_input_addon.bpy.operator.file_input_rule_operator import FILEINPURULE_OT_apply_on_scene

    register_class(FILEINPURULE_OT_apply_on_scene)
    register_class(FILEINPUTLIST_OT_entry_add)
    register_class(FILEINPUTLIST_OT_entry_remove)
    register_class(FILEINPUTLIST_OT_entry_move)

def unregister_operators():
    from bpy.utils import unregister_class

    from ocio_file_input_addon.bpy.operator.file_input_list_operator import (
        FILEINPUTLIST_OT_entry_add, FILEINPUTLIST_OT_entry_remove,
        FILEINPUTLIST_OT_entry_move
    )

    from ocio_file_input_addon.bpy.operator.file_input_rule_operator import FILEINPURULE_OT_apply_on_scene

    unregister_class(FILEINPURULE_OT_apply_on_scene)
    unregister_class(FILEINPUTLIST_OT_entry_add)
    unregister_class(FILEINPUTLIST_OT_entry_remove)
    unregister_class(FILEINPUTLIST_OT_entry_move)
