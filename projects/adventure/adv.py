from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

player = Player(world.starting_room)
# You may find the commands `player.current_room.id`, `player.current_room.get_exits()` 
# and `player.travel(direction)` useful
# Fill this out with directions to walk
# traversal_path = ['n', 'n']
reverse = {'n':'s','s':'n','e':'w','w':'e'}
def traverse_recursive(start, visited=None, path=None):

    # is visited is none set it to a set
    if visited is None:
        visited = set()
    #if path is none set it to array/list
    if path is None:
        path = []

    # travel down a path
    # print(path)
    for direction in player.current_room.get_exits():
        player.travel(direction)
        # look from starting room and see if its in visited:
        # not in visited list
        if player.current_room.id not in visited: 
            # add it to visited
            visited.add(player.current_room.id)
            #add where we traveld
            path.append(direction)
            # repeat
            traverse_recursive(player.current_room.id, visited, path)
            # return to starting
            player.travel(reverse[direction])
            # add it same way as travel
            path.append(reverse[direction])
        # if its already been visited then we want to reverse our order
        # and travel in the opposite direction
        else:
            player.travel(reverse[direction])
    # print('this is visited', visited)
    # print('this is path', path)
    return path

traversal_path = traverse_recursive(player.current_room.id)  
 
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
