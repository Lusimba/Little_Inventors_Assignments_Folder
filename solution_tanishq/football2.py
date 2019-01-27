class Player(object):
    def __init__(self,first,last,position,jersey,club):
        self.first = first
        self.last = last
        self.position = position
        self.jersey = jersey
        self.club = club

Player_1 = Player("Lionel","Messi","RW",10,"FC Barcelona")
print (Player_1)