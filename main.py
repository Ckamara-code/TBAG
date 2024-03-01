from room import Room
from character import Enemy
from character import Friend
from key import Key


kitchen = Room("kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies")
ballroom = Room("ballroom")
ballroom.set_description("a large, hollow, well-decorated room")
dining_hall = Room("dining hall")
dining_hall.set_description("A room with a dining table and chairs")

ballroom_key = Key(ballroom)
ballroom_key.location = kitchen

ballroom.lock_room(ballroom_key)



kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom,"west")
ballroom.link_room(dining_hall,"east")


dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("cheese")

paul = Enemy("Paul", "An extraterrestrial Dragon")
paul.set_conversation("Hissss")
paul.set_weakness("ice")

dining_hall.set_character(dave)
kitchen.set_character(paul)


current_room = kitchen



while True:
    print("\n")
    
    
    
    inhabitant = current_room.get_character()

    if inhabitant is not None: 
        inhabitant.describe()
    
    command = input("> ")

    if command in ["north", "south", "east", "west"]:
            current_room = current_room.move(command)
            current_room.get_details()
            

    elif command == "find key":
        ballroom_key.find_key(current_room)

    elif command == "unlock room":
        print(ballroom.unlock_room(ballroom_key,ballroom))
        
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()

    elif command == "fight":
        if isinstance(inhabitant, Enemy) == True:
            current_item = input("What item would you like to fight with ")
            
            if inhabitant.fight(current_item) == False:
                quit()

    elif command == "bribe":
        if isinstance(inhabitant, Enemy) == True:
            if inhabitant is not None:
                inhabitant.bribe()

        else:
            print("You can not bribe" + inhabitant.name)
                

    elif command == "steal":
        if isinstance(inhabitant, Enemy) == True:
            inhabitant.steal()
        
        else:
            print("You cannot steal from " + inhabitant.name)


    elif command == "send to sleep":
        if isinstance(inhabitant, Enemy) == True:
            inhabitant.send_to_sleep()

        else:
            print("You cannot send " + inhabitant.name + "to sleep")
            

    elif command == "hug":
        if isinstance(inhabitant, Friend) == True:
            inhabitant.hug()

        else:
            print(inhabitant.name + " does not want to hug you.")


                




