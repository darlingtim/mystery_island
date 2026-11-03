
class Game:
    def __init__(self):
        self.is_running = False
        self.player = None
        self.won = False
        self.lose = False

    def __wonSetter(self):
        if self.won == False:
            self.won = True
        elif self.won == True:
            self.won = False

    def __loseSetter(self):
        if self.lose == False:
            self.lose = True
        elif self.lose == True:
            self.lose = False


    def quit_game(self, player):
        self.is_running = False
        return f"GoodBye {player.name}!, You can always come back to explore Mystery Island."

    def start_game(self, player):
        if self.won == False and self.lose == False and self.is_running == False:
            self.is_running = True
            self.player = player
            print(f"Lets Play {player.name}!, You have {player.energy} energy to explore the island.")
            
        else:
            return "Game is already running."
        

    def replay_game(self, player):
        if (self.won == True or self.lose == True) and self.is_running == False:
            if self.won == True:
                self.__wonSetter()
            if self.lose == True:
                self.__loseSetter()

        
            player.energy += 5
            self.player = player
            self.start_game(player)

        else:
            return "Game is already running."




        