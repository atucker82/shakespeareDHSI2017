from src.Parser.LineOfDialogue import LineOfDialogueParser
from src.parts.parts import Scene
import re

class SceneParser(object):

    SCENE_HEADING_PATTERN = re.compile(
        r"SCENE\s(?P<scene_number>[0-9VIX]*)\."
    )

    def __init__(self, parent, line_of_text): #creates object that contains self, its parent and a line of text
        self.parent = parent
        parsing_results = self.SCENE_HEADING_PATTERN.match(line_of_text).groupdict()
        self.scene = Scene(
            parsing_results["scene_number"]
        )

    def parse(self, text): # creates parse as a function
        if text == "":
            return self
        elif LineOfDialogueParser.NEW_LINE_PATTERN.match(text):
            parser = LineOfDialogueParser(
                self, text
            )
            self.scene.lines_of_dialogue.append(
                parser.dialogue
            )
            return parser
        elif self.SCENE_HEADING_PATTERN.match(text):
            return self.parent
        else:
            return self
