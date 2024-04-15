import bpy
from bpy.app.handlers import persistent

from ocio_file_input_addon.bpy.property.file_input_property import FileInputRuleProperty

@persistent
def add_default_file_rule_if_not_exists(_):
    for file_rule in bpy.context.scene.file_input_list:
        if file_rule.name == "Default":
            return
    
    file_input_rule_default = bpy.context.scene.file_input_list.add()
    file_input_rule_default.name = "Default"
    file_input_rule_default.colorspace = "Non-Color"
    file_input_rule_default.pattern = "*"
    file_input_rule_default.extension = "*"
    file_input_rule_default.deletable = False


def register_properties():
    bpy.utils.register_class(FileInputRuleProperty)
    bpy.types.Scene.file_input_list = bpy.props.CollectionProperty(type=FileInputRuleProperty)
    bpy.types.Scene.file_input_list_index = bpy.props.IntProperty()

    bpy.app.handlers.load_post.append(add_default_file_rule_if_not_exists)

def unregister_properties():
    bpy.utils.unregister_class(FileInputRuleProperty)
    bpy.app.handlers.load_post.remove(add_default_file_rule_if_not_exists)
    del bpy.types.Scene.file_input_list
    del bpy.types.Scene.file_input_list_index