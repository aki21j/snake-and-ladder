import uuid

class Player:

  def __init__(self, name=None, position=None) -> None:
      self.name = name
      self.id = uuid.uuid4()
      self.position = position
      self.is_winner = False

  def get_name(self):
    return self.name
  
  def get_id(self):
    return self.id

  def get_position(self):
    return self.position

  def set_name(self, name):
    self.name = name
  
  def set_id(self, id):
    self.id = id

  def set_position(self, position):
    self.position = position

  def move_player(self, dice_value, encounter = None):
    """
    move player and update position
    if encounter, snake or ladder, print msg and update position
    """
    new_position = dice_value
    if not encounter:
      print("Player {} rolled: {}".format(self.name, dice_value))
      new_position = self.position + dice_value

    if new_position > 100:
      print("Player {} has moved from {} to {} -> OUT OF BOUNDS!".format(self.name, self.position, new_position))
      return
    elif new_position == 100:
      self.is_winner = True
    
    print("Player {} has moved from {} to {}".format(self.name, self.position, new_position))
    self.position = new_position
    
