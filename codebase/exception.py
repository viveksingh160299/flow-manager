class dbException(Exception):
   def __init__(self, message):
      self.message = message
      super().__init__(self.message)

   def __str__(self):
      return str(self.message)


class flowManagerException(Exception):
   def __init__(self, message):
      self.message = message
      super().__init__(self.message)

   def __str__(self):
      return str(self.message)



class authException(Exception):
   def __init__(self, message):
      self.message = message
      super().__init__(self.message)

   def __str__(self):
      return str(self.message)