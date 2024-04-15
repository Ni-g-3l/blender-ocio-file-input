def register_panels():
    from bpy.utils import register_class

    from ocio_file_input_addon.bpy.panel.file_input_panel import RENDER_PT_file_input_panel
    from ocio_file_input_addon.bpy.panel.file_input_list import FILE_UL_file_input
    
    register_class(FILE_UL_file_input)
    register_class(RENDER_PT_file_input_panel)
    
def unregister_panels():
    from bpy.utils import unregister_class
    
    from ocio_file_input_addon.bpy.panel.file_input_panel import RENDER_PT_file_input_panel
    from ocio_file_input_addon.bpy.panel.file_input_list import FILE_UL_file_input
    
    unregister_class(FILE_UL_file_input)
    unregister_class(RENDER_PT_file_input_panel)