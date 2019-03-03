from termcolor import colored

class Box:
  def __init__(self, box_number):
    self.box_number = box_number
    self.filled = False
    self.value = False

  def fill(self, player_value):
    self.filled = True
    self.value = player_value

  def print_box(self):
    if self.value == "X":
      return colored(' X ', 'green')
    elif self.value == "O":
      return colored(' O ', 'blue')
    else:
      return '[ ]'

  def explain(self):
    print "I am a box"
    print "My number is {0}".format(self.box_number)
    print "My value is {0}".format(self.value)
    print "Am I filled? {0}".format(self.filled)
