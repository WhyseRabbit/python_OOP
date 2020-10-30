class Character:
    """This is a basic fantasy character generator with five basic attributes:
        name = String; this is the name of the character
        might = Integer; this is considered stregth and stamina
        finse = Integer; Shortcut to 'finesse' is considered agility
        mind = Integer; wherewithal and ability to think quickly
        charm = Integer; ability to connect with other people"""

    def __init__(self, name : str = None, might : int = 5,
                 finesse : int = 5, mind : int = 5,
                 charm : int = 5):
    self.name = name
    self.might = might
    self.finse = finesse
    self.mind = mind
    self.charm = charm

