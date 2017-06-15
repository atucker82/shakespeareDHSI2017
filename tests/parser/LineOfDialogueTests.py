import unittest

from src.Parser.LineOfDialogue import LineOfDialogueParser
from src.Parser.SceneParser import SceneParser


class LineOfDialogueParserTests(unittest.TestCase):

    #Tests whether parser seperates and identifies character name and a line of dialogue in a example line of dialogue
    def test_create_new_line_of_dialogue_parent_and_dialogue(self):
        scene_parser = SceneParser() #passes in the object SceneParser from src
        text = "  FIRST LORD. Our remedies oft in ourselves do lie," #example text for test
        parser = LineOfDialogueParser( #brings in LineOfDialogue from src and attritbes it to parser
            scene_parser, text # parse is now a string that contains scene_parser (the object SceneParser()) and text
        )
        self.assertEqual(
            parser.parent, scene_parser
        )
        self.assertEqual(
            parser.dialogue.character_name, "FIRST LORD"
        )
        self.assertEqual(
            parser.dialogue.lines,[
                "Our remedies oft in ourselves do lie,"
            ]
        )

    def test_add_new_line_of_text_appends_to_existing_dialogue(self):
        scene_parser = SceneParser()
        text = "   HELENA. Our remedies oft in ourselves do lie,"
        parser = LineOfDialogueParser(
            scene_parser, text
        )
        parser.parse("    which we ascribe to heaven, the fated say")
        self.assertEqual(
            parser.dialogue.lines,[
                "Our remedies oft in ourselves do lie,",
                "which we ascribe to heaven, the fated say",
            ]
        )

    def test_add_additional_lines_appends_to_current_dialogue(self):
        scene_parser = SceneParser()
        text = "  HELENA. Our remedies oft in ourselves do lie,"
        parser = LineOfDialogueParser(
            scene_parser, text
        )
        parser.parse("    which we ascribe to heaven, the fated say")
        parser.parse("    Gives us free scope, only doth backwards pull")
        self.assertEqual(
            parser.dialogue.lines,[
                "Our remedies oft in ourselves do lie,",
                "which we ascribe to heaven, the fated say",
                "Gives us free scope, only doth backwards pull",
                 ]
        )

    def test_handles_new_character_name(self):
        text = "  HELENA. Our remedies oft in ourselves do lie,"
        scene_parser = SceneParser()
        parser = LineOfDialogueParser(
            scene_parser, text
        )
        parser.parse("    which we ascribe to heaven. The fated say")
        parser.parse("    Gives us free scope, only doth backwards pull")
        parser.parse("  PAROLLES. I am so full of bussiness I cannot answer")
        self.assertEqual(
            parser.dialogue.lines,[
                 "Our remedies oft in ourselves do lie,",
                 "which we ascribe to heaven. The fated say",
                 "Gives us free scope, only doth backwards pull",
            ]
        )
        #TO_DO: Implement handling creation of new line of dialogue parser



