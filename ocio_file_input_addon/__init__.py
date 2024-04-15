

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
    from ocio_file_input_addon.bpy.property import register_properties
    register_properties()
    
    from ocio_file_input_addon.bpy.operator import register_operators
    register_operators()
    
    from ocio_file_input_addon.bpy.panel import register_panels
    register_panels()

def unregister():
    from ocio_file_input_addon.bpy.property import unregister_properties
    unregister_properties()

    from ocio_file_input_addon.bpy.operator import unregister_operators
    unregister_operators()

    from ocio_file_input_addon.bpy.panel import unregister_panels
    unregister_panels()
