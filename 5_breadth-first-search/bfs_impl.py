from bfs_graph import graph
from collections import deque

def person_is_seller(name): # treat all people who have names ending with 'm' as mango sellers for sake of example
    return name[-1] == 'm'

def bfs_search(name):
    search_queue = deque()  # create queue
    search_queue += graph["you"]  # add all neigbours to me to the queue
    searched = []   # array to keep track of who is searched
    while search_queue:  # while queue is not empty
        person = search_queue.popleft()  # grab first person off the queue; see https://pythontic.com/containers/deque/popleft
        if not person in searched:
            if person_is_seller(person):    # check whether he/she is mango seller
                print(person + " is a mango seller!")
                return True
            else:
                # not seller, add all friends of this person to queue
                search_queue += graph[person]
    return False    # no one was queue in all networks

bfs_search("you")