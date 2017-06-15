# Let's start by defining a class called "Play". The thing in parentheses
class Play(object):

    # now we'll start to assign all the attributes that a play has
    # we're going to define this play by reading through lines of text.
    def __init__(self, title):
        # here is how to recognise the title of the play, when you are reading through lines of text
        self.title = title
        # initialised to an empty list
        self.acts = []

# we need to be able to recognise an Act
class Act(object):

    def __init__(self, number):
        self.number = number
        self.scenes = []

class Scene(object):

    def __init__(self, number):
        self.number = number
        self.lines_of_dialogue = []

class LineOfDialogue(object):

    def __init__(self, character_name):
        self.character_name = character_name
        self.lines = []
