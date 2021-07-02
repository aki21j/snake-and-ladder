from random import randint
class Dice:

  def __init__(self) -> None:
      self.value = None

  def roll(self):
    self.value = randint(1,6)
    return self.value