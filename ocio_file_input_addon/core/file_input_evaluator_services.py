import collections
import fnmatch
import os


FileInputRule = collections.namedtuple(
    "FileInputRule", "name extension pattern colorspace"
)

class FileInputEvaluatorService:

    DEFAULT_RULE = FileInputRule("Default", "*", "*", "raw")

    def __init__(self, rules:list = None) -> None:
        if not rules:
            rules = []
        self._rules = rules

    def eval(self, filepath) -> str:
        for rule in self._rules:
            if self._file_is_matching_rule(rule, filepath):
                return rule.colorspace
        return self.DEFAULT_RULE.colorspace
    
    def _file_is_matching_rule(self, rule, filepath):
        file_basename = os.path.basename(filepath)
        file_ext = os.path.splitext(file_basename)[-1]
        file_name = os.path.splitext(file_basename)[0]
        ext_match = rule.extension == self.DEFAULT_RULE.extension or rule.extension == file_ext
        name_match = rule.pattern == self.DEFAULT_RULE.pattern or fnmatch.fnmatch(file_name, rule.pattern)
        return ext_match and name_match