from random import randrange, choice

class Player:
  def __init__(self, symbol):
    self.symbol = symbol

  def other_symbol(self):
    if self.symbol == "X":
      return "O"
    else:
      return "X"

  def join_game(self, game):
    self.game = game

  def next_winning_choices(self):
    empties = self.game.empty_boxes()
    winners = []
    blocked_winners = []

    for i, move in enumerate(empties):
      g = self.game.generate_hypothetical(self.symbol, move)
      if g.is_won():
        return move

      blocked_game = self.game.generate_hypothetical(self.other_symbol(), move)
      if blocked_game.is_won():
        blocked_winners.append(move)

    if len(blocked_winners):
      return blocked_winners[0]
    return False

  def next_choice(self):
    winner = self.next_winning_choices()
    if winner:
      return winner

    empties = self.game.empty_boxes()
    return choice(empties)

class HumanPlayer(Player):
  def next_choice(self):
    choice = input("Where would you like to go? ")
    if self.is_valid(choice):
      return int(choice)
    else:
      print "Bad answer, try again"
      return self.next_choice()

  def is_valid(self, choice):
    if int(choice) > -1 and int(choice) < 9:
      if not(self.game.boxes[int(choice)].filled):
        return True

    return false
