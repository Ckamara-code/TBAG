
class Room():
   def __init__(self, room_name):
      self.name = room_name
      self.description = None
      self.linked_rooms = {}
      self.character = None
      self.is_locked = None

   def get_description(self):
      return self.description
   
   def set_description(self, room_description):
      self.description = room_description

   def describe(self):
      print(  self.description  )

   def set_name(self, room_name):
      self.name = room_name

   def get_name(self):
      return self.name

   def link_room(self, room_to_link, direction):
      self.linked_rooms[direction] = room_to_link

   def get_details(self):
      print(self.name)
      print("-------------------------")
      print(self.description)
      for direction in self.linked_rooms:
         room = self.linked_rooms[direction]
         print("The " + room.get_name()+ " is "+direction)

   def move(self,direction):
      if direction in self.linked_rooms:
         if self.linked_rooms[direction].is_locked is not True:

            return self.linked_rooms[direction]
         else: 
            print("You can't go that way. The room is locked.")
            return self
      else:
         print("You can't go that way")
         return self
      
   def set_character(self, new_character):
      self.character = new_character
      
   def get_character(self):
      return self.character
   
   def lock_room(self,key):
      if key.key_type.name == self.name:
         
         self.is_locked = True
         return str(self.name + "is locked")

      else:
         return str("could not lock " + self.name + "with" + key.key_type.name)
      
   def unlock_room(self,key,room_to_unlock):
      if room_to_unlock.name == key.key_type.name:
         if key.player_possessed == True:
            self.is_locked = False
            return str(self.name + " is unlocked")
         
         else:
            return str("You need to find the key")

      else:
         return str("You need to find the key")