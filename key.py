from item import Item

class Key(Item):
    def __init__(self, key_type):
        super().__init__()
        self.key_type = key_type
        
    def get_key_type(self):
        return self.key_type
    
    def find_key(self, current_room):
        if current_room.name == self.location.name:
            print("You have collected a key")
            self.possess_item()

        else:
            print("No key is found")

            