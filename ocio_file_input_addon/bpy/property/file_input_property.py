import bpy

COLORSPACES = None

def get_colorspaces(_, context):
    """
    Extract colorspace from Scene Enum properties
    """
    global COLORSPACES
    if COLORSPACES:
        return COLORSPACES
    colorspace_items = (
        type(context.scene)
        .bl_rna.properties["sequencer_colorspace_settings"]
        .fixed_type.properties["name"]
        .enum_items
    )
    available_colorspaces = []
    for index, colorspace in enumerate(colorspace_items):
        available_colorspaces.append(
            (
                colorspace.identifier,
                colorspace.name,
                colorspace.description,
                "",
                index,
            )
        )
    COLORSPACES = available_colorspaces
    return COLORSPACES


class FileInputRuleProperty(bpy.types.PropertyGroup):
    name: bpy.props.StringProperty()
    extension: bpy.props.StringProperty()
    pattern: bpy.props.StringProperty()
    colorspace: bpy.props.EnumProperty(
        items=get_colorspaces
    )
