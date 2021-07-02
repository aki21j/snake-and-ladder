class Snake:

  def __init__(self, start, end) -> None:
      self.start = start
      self.end = end
      self.message = "SNAKE BITE -> goto: {}".format(self.end)

  def get_start(self):
    return self.start
  
  def get_end(self):
    return self.end

  def set_start(self, start):
    self.start = start

  def set_end(self, end):
    self.end = end