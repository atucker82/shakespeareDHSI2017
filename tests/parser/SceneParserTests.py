import unittest

from src.Parser.ActParser import ActParser
from src.Parser.LineOfDialogue import LineOfDialogueParser
from src.Parser.SceneParser import SceneParser

class SceneParserTests(unittest.TestCase):

    def test_recognizes_line_of_dialogue(self):
        scene_parser = SceneParser(None, "SCENE I.")  # passes in the object SceneParser from src, similar to the test for line of dialogue that recognizes new line of dialogue
        text = "  FIRST LORD. Our remedies oft in ourselves do lie,"  # example text for test
        new_parser = scene_parser.parse(text) #creates new parser that will parse the line text
        if isinstance(new_parser, LineOfDialogueParser): #is this new parser our line of dialogue parser?
            self.assertTrue(True) #if it is, we did it!
        else:
            self.fail()

    def test_skips_over_lines_that_are_not_dialogue_lines(self):
        scene_parser = SceneParser(None, "SCENE IV.")  # passes in the object SceneParser from src
        stage_direction = "Enter BERTRAM, the COUNTESS OF ROUSILLON, HELENA, and LAFEU, all in black"
        new_parser = scene_parser.parse(stage_direction)
        self.assertEqual(new_parser, scene_parser)

    def test_parser_skips_blank_line(self):
        scene_parser = SceneParser(None, "SCENE III.")
        blank_line = ""
        new_parser = scene_parser.parse(blank_line)
        self.assertEqual(new_parser, scene_parser)

    def test_parser_skips_exit_line(self):
        scene_parser = SceneParser(None, "SCENE VI.")
        exit_line = "Exit"
        new_parser = scene_parser.parse(exit_line)
        self.assertEqual(new_parser, scene_parser)

    def test_recognizes_start_of_scene_with_arabic_numeral(self):
        start_of_scene = "SCENE 4."
        scene_parser = SceneParser(None, start_of_scene)  # passes in the object SceneParser from src
        new_parser = scene_parser.parse(start_of_scene)
        self.assertEqual(scene_parser.scene.number, "4")

    def test_start_of_scene_with_roman_numeral(self):
        start_of_scene = "SCENE IV."
        scene_parser = SceneParser(None, start_of_scene)  # passes in the object SceneParser from src
        new_parser = scene_parser.parse(start_of_scene)
        self.assertEqual(scene_parser.scene.number, "IV")

    def test_recognizes_end_of_scene(self):
        start_of_scene = "SCENE IV."
        act_parser = ActParser(None, "ACT I.")
        scene_parser = SceneParser(act_parser, start_of_scene)
        start_of_new_scene = "SCENE V."
        next_parser = scene_parser.parse(start_of_new_scene)
        if isinstance(next_parser, ActParser):
            self.assertTrue(True)
        else:
            self.fail()



