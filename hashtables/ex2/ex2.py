#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    route = []
    flight = {}

    # loop through tickets to make table, set source as key, set destination as value
    for i in range(length):
        key = tickets[i].source
        value = tickets[i].destination

        #link source as key to destination
        flight[key] = value   

    # set start of route where key is NONE
    key = flight["NONE"]

    # run the rest of the route whle key is not None
    while key != "NONE":
        # add to route list
        route.append(key)
        # determine the next destination
        key = flight[key]

    # key has a value of NONE so while loop doesn't run 
    # tests include NONE as last index so append
    route.append(key)
    
    return route
        


tickets = [    
    Ticket( "PIT", "ORD" ),
    Ticket( "XNA", "CID" ),
    Ticket( "SFO", "BHM" ),
    Ticket( "FLG", "XNA" ),
    Ticket( "NONE", "LAX" ),
    Ticket( "LAX", "SFO" ),
    Ticket( "CID", "SLC" ),
    Ticket( "ORD", "NONE" ),
    Ticket( "SLC", "PIT" ),
    Ticket( "BHM", "FLG" )
]

print(reconstruct_trip(tickets, 10))

# plan

# set source and destination as key value pair
# route is set by matching previous destination to source
# start trip at source none
# append matching prev destination to curr source until destination is none