import unittest

from ocio_file_input_addon.core.file_input_evaluator_services import FileInputEvaluatorService, FileInputRule

class Test_ocio_file_input_addon(unittest.TestCase):

    def test_return_default_rule_on_empty_rule_list(self):
        evaluator = FileInputEvaluatorService()
        self.assertEqual("raw", evaluator.eval("/tmp/salut.exr"))
        evaluator = FileInputEvaluatorService([])
        self.assertEqual("raw", evaluator.eval("/tmp/salut.exr"))

    def test_return_colorspace_based_on_extension(self):
        ext_rule = FileInputRule("EXR Rule", ".exr", "*", "srgb")
        evaluator = FileInputEvaluatorService([ext_rule])
        self.assertEqual("srgb", evaluator.eval("/tmp/salut.exr"))
        ext_rule = FileInputRule("PNG Rule", ".png", "*", "srgb")
        evaluator = FileInputEvaluatorService([ext_rule])
        self.assertEqual("raw", evaluator.eval("/tmp/salut.exr"))

    def test_return_colorspace_based_on_name(self):
        name_rule = FileInputRule("SRGB File name Rule", "*", "*-srgb", "srgb")
        evaluator = FileInputEvaluatorService([name_rule])
        self.assertEqual("srgb", evaluator.eval("/tmp/salut-srgb.exr"))
        evaluator = FileInputEvaluatorService([name_rule])
        self.assertEqual("raw", evaluator.eval("/tmp/salut-linear.exr"))

    def test_return_colorspace_with_multiple_rules_based_on_order(self):
        evaluator = FileInputEvaluatorService([
            FileInputRule("SRGB File name Rule", "*", "*-srgb", "srgb"),
            FileInputRule("EXR Rule", ".exr", "*", "acescg")
        ])
        self.assertEqual("acescg", evaluator.eval("/tmp/salut-srgb.exr"))

        evaluator = FileInputEvaluatorService([
            FileInputRule("SRGB File name Rule", "*", "*-srgb", "srgb"),
            FileInputRule("EXR Rule", ".exr", "*", "acescg")
        ])
        self.assertEqual("srgb", evaluator.eval("/tmp/salut-srgb.tiff"))
        
        evaluator = FileInputEvaluatorService([
            FileInputRule("SRGB File name Rule", "*", "*-srgb", "srgb"),
            FileInputRule("EXR Rule", ".exr", "*", "acescg")
        ])
        self.assertEqual("raw", evaluator.eval("/tmp/salut-linear.jpeg"))
