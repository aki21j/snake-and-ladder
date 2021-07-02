from snake import Snake
from ladder import Ladder

class Board:

  def __init__(self, size=100) -> None:
    self.board = [None for i in range(size+1)]

  def populate(self, snakes: "list[Snake]", ladders:"list[Ladder]"):
    for snake in snakes:
      start = snake.get_start()
      self.board[start] = snake

    for ladder in ladders:
      start_point = ladder.get_start()
      self.board[start_point] = ladder

    return self.board