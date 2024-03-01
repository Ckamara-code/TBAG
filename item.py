class Item():

    def __init__(self):
        self.name = None
        self.description = None
        self.location = None
        self.player_possessed = False

    def get_name(self, name):
        self.name = name

    def set_name(self, name):
        return self.name
    
    def get_description(self):
        return self.description

    def set_description(self, item_description):
        self.description = item_description

    def get_location(self):
        return self.location
    
    def set_location(self,location):
        self.location = location

    def possess_item(self):
        self.player_possessed = True


