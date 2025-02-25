from django.db import models

# Create your models here.

class Rectangle:

    def __init__(self , length:int , breadth:int):
        self.length = length
        self.breadth = breadth

    def iterater(self):
        yield(self.length)    
        yield(self.breadth)    
  
