from ladder import Ladder
from player import Player
from snake import Snake
from dice import Dice
from board import Board


class Game:
  def __init__(self) -> None:
      self.winner = None

  def play(self, snakes:"list[Snake]", ladders: "list[Ladder]", players: "list[Player]"):
    turns = 0

    board = Board().populate(snakes, ladders)
    dice = Dice()

    while not self.winner:
      turns += 1
      
      print("\n--------------Turn : {}--------------".format(turns))

      for player in players:
        
        dice_value = dice.roll()
        new_position = dice_value
        six_count = 0

        while dice_value == 6:
          six_count += 1
          dice_value = dice.roll()
          if six_count != 2:
            new_position += dice_value
          else:
            new_position = dice_value
            six_count = 0

        player.move_player(new_position)

        encounter: Snake = board[player.position]

        if encounter:
          end_point = encounter.end
          print("--ENCOUNTER : {}".format(encounter.message))
          player.move_player(end_point, True)

        if player.is_winner:
          self.winner = player
          break


    print("\n--------------GAME OVER--------------")
    print(f"Player {self.winner.name} Has won the game after {turns} turns")
    print("--------------GAME OVER--------------\n")



if __name__ == "__main__":
  snakes = [Snake(7,3) , Snake(37,13) , Snake(80,60)]
  ladders = [Ladder(1,27) , Ladder(33,60) , Ladder(70,79)]

  # hard coded details for 2 players
  players = [ Player("A" , 1), Player("B" , 1)]
  game = Game()
  game.play(snakes, ladders, players)
