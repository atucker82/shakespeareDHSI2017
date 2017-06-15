import unittest

from src.Parser.ActParser import ActParser
from src.Parser.PlayParser import PlayParser
from src.Parser.SceneParser import SceneParser


class ACtParserTests(unittest.TestCase):

    def test_create_act_parser_recognizes_parent_and_number(self):
        play_parser = PlayParser(None, "THE REVENGE OF THE DHSI BUNNIES")
        act_parser = ActParser(play_parser, "ACT I. SCENE 4.")
        self.assertEqual(act_parser.parent, play_parser)
        self.assertEqual(act_parser.act.number, "I")

    def test_act_parser_recognizes_act_and_scene_heading(self):
        play_parser = PlayParser(None, "THE REVENGE OF THE DHSI BUNNIES")
        act_parser = ActParser(play_parser, "ACT I. SCENE I.")
        next_parser = act_parser.parse("ACT I. SCENE I.")
        self.assertIsInstance(next_parser, SceneParser)

    def test_create_act_parser_recognizes_new_scene(self):
        act_parser = ActParser(None, "ACT I.")
        scene_heading = "SCENE 1."
        next_parser = act_parser.parse(scene_heading)
        self.assertIsInstance(next_parser, SceneParser)

    def test_create_act_parser_recognizes_end_of_scene(self):
        play_parser = PlayParser(None, "THE REVENGE OF THE DHSI BUNNIES")
        act_parser = ActParser(play_parser, "ACT I. SCENE III.")
        next_parser = act_parser.parse("ACT II. SCENE 1.")
        self.assertIsInstance(next_parser, PlayParser)
        self.assertEqual(next_parser, play_parser)