from itertools import cycle
import pdb

from box import Box
from player import Player, HumanPlayer

class Game:
  win_conditions = [
    [0,1,2], [3,4,5], [6,7,8],
    [0,3,6], [1,4,7], [2,5,8],
    [0,4,8], [2,4,6]
  ] # These are the lines!

  def __init__(self, player1, player2):
    self.boxes = []
    for i in range(9):
      self.boxes.append(Box(i))

    self.players = [player1, player2]
    self.players_cycle = cycle(self.players)
    self.current_player = next(self.players_cycle)
    self.game_over = False

  def generate_hypothetical(self, symbol, box_index):
    new_game = Game(self.players[0], self.players[1])
    for box in self.boxes:
      if (box.filled):
        new_game.boxes[box.box_number].fill(box.value)
    new_game.boxes[box_index].fill(symbol)
    return new_game

  def is_won(self):
    if len(self.empty_boxes()) == 0:
      self.game_over = True
      return True

    for condition in self.win_conditions:
      if self.line_is_won(condition):
        self.game_over = True
    return self.game_over

  def empty_boxes(self):
    empty_boxes = filter(lambda b: not(b.filled), self.boxes)
    empty_indeces = map(lambda b: b.box_number, empty_boxes)
    return empty_indeces

  def line_is_won(self, line):
    boxes = map(lambda i: self.boxes[i].value, line)
    p1 = self.players[0].symbol
    p2 = self.players[1].symbol

    if boxes == [p1, p1, p1]:
      return True
    if boxes == [p2, p2, p2]:
      return True
    return False

  def print_board(self):
    for x in [0, 1, 2]:
      row = []
      for y in [0, 1, 2]:
        index = x + (y * 3)
        sq = self.boxes[index]
        row.append(sq.print_box())
      string = ''.join(row)
      print string

    if self.is_won():
      print "Game over!"
    print ""

  def take_turn(self):
    if self.is_won():
      return # Don't take a turn if the game is over
    box_index = self.current_player.next_choice()
    if self.boxes[box_index].filled:
      return

    self.make_move(self.current_player, box_index)
    self.current_player = next(self.players_cycle) # alternate turns
    self.print_board() # display

  def make_move(self, player, box_index):
    box = self.boxes[box_index]
    if box.filled:
      return # Don't take a turn if the selected box is already filled
    box.fill(player.symbol)

p1 = Player('X')
p2 = Player('O')
g = Game(p1, p2)

p1.join_game(g)
p2.join_game(g)

while not(g.is_won()):
  g.take_turn()
