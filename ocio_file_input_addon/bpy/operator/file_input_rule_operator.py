import bpy

from ocio_file_input_addon.core.file_input_evaluator_services import FileInputEvaluatorService

class FILEINPURULE_OT_apply_on_scene(bpy.types.Operator):
    """Apply file input rule to scene"""

    bl_idname = "fileinputlist.file_input_apply_on_scene"
    bl_label = "Apply File Input Rule on Scene"

    def execute(self, context):
        service = FileInputEvaluatorService(context.scene.file_input_list)

        for image in bpy.data.images:
            new_colorspace = service.eval(image.filepath)
            self.report({"INFO"}, "Change Image '{}' Colorspace to '{}'".format(image.name, new_colorspace))
            image.colorspace_settings.name = new_colorspace

        return {'FINISHED'}
