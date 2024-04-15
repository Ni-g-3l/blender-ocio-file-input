import bpy


class FILE_UL_file_input(bpy.types.UIList):

    def draw_filter(self, context, layout):
        pass

    def filter_items(self, context, data, propname):
        flt_flags = []
        flt_neworder = []
        return flt_flags, flt_neworder
