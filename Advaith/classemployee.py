class Players:
    def __init__(self, first, last, position):
        self.firstname = first
        self.surname = last
        self.play = position
    def greeting(self):
        print("Hi I am %s and my last name is %s and I play as %s" %(self.firstname, self.surname, self.play))
plr_1 = Players('Advaith', 'Yellai', 'Center Defence Mid')
plr_2 = Players('Wojciech', 'Szczresny', 'Goalkeeper')
plr_3 = Players('Christiano', 'Ronaldo', 'Right Forward')
plr_4 = Players('Paula', 'Dybala', 'Left Forward')
plr_5 = Players('Miralem', 'Pjanic', 'Center Attack mid')
plr_6 = Players('Douglas', 'Costa', 'Right Wing')
plr_7 = Players('Emre', 'Can', 'Left wing')
plr_8 = Players('Medhi','Benatia','Right front defence')
plr_9 = Players('Leornado','Bonicci','Left front defence')
plr_10 = Players('Joao','Cancelo','Right back defence')
plr_11 = Players('Giorgio','Chiellini','Left back defence')
plr_1.greeting()
plr_2.greeting()
plr_3.greeting()
plr_4.greeting()
plr_5.greeting()
plr_6.greeting()
plr_7.greeting()
plr_8.greeting()
plr_9.greeting()
plr_10.greeting()
plr_11.greeting()