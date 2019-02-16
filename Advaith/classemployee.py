class Player:
    def __init__(self, first, last, position):
        self.firstname = first
        self.surname = last
        self.play = position
    def greet(self):
        print("Hi I am %s and my last name is %s and I play as %s" %(self.firstname, self.surname, self.play))

plr_1 = Player('Advaith   ', 'Yellai   ', 'Center Defence Mid')
plr_2 = Player('Wojciech  ', 'Szczresny', 'Goalkeeper        ')
plr_3 = Player('Christiano', 'Ronaldo  ', 'Right Forward     ')
plr_4 = Player('Paulo     ', 'Dybala   ', 'Left Forward      ')
plr_5 = Player('Miralem   ', 'Pjanic   ', 'Center Attack mid ')
plr_6 = Player('Douglas   ', 'Costa    ', 'Right Wing        ')
plr_7 = Player('Emre      ', 'Can      ', 'Left wing         ')
plr_8 = Player('Medhi     ', 'Benatia  ','Right front defence')
plr_9 = Player('Leornado  ', 'Bonucci  ','Left front defence ')
plr_10 = Player('Joao     ', 'Cancelo  ','Right back defence ')
plr_11 = Player('Giorgio  ', 'Chiellini','Left back defence  ')

plr_1.greet()
plr_2.greet()
plr_3.greet()
plr_4.greet()
plr_5.greet()
plr_6.greet()
plr_7.greet()
plr_8.greet()
plr_9.greet()
plr_10.greet()
plr_11.greet()