import tkinter
import MLB_stats_builder as mlbb

class Application:
    def __init__(self):
        self.window1 = tkinter.Tk()
        self.window1.title('Batting Stats Widget')
        self.window1.resizable(False, False) 
        self.label = tkinter.Label(master=self.window1, text = "Enter the name of an MLB player:",
                                   background = '#FFFFFF')
        self.label.grid(row = 0,column=0, sticky = tkinter.W)
        self.button = tkinter.Button(master= self.window1, text = 'Enter')
        self.button.grid(row = 0, column = 5,sticky = tkinter.W)
        self.button.bind('<Button-1>', self.get_player)
        self.textBox=tkinter.Entry(master = self.window1)
        self.textBox.grid(row=0,column=4, sticky = tkinter.E)
        
    def get_player(self,event):
        player = self.textBox.get()
        print(type(player))
        self.display_stats(player)

    def display_stats(self,player:str):
        #self.window1.kill()
        try:
            self.label2.destroy()
        except:
            pass
        self.window1.title(mlbb.proper_name(player))
        last_name_url = mlbb.last_name_url(player)
        #print(last_name_url)
        last_name_source = mlbb.get_source(last_name_url)
        #print(last_name_source)
        #text_output = open('Output.txt','w')
        try:
            player_url = mlbb.get_player_url(player,last_name_source)
            #print(mlbb.get_source(player_url))
            stats = mlbb.parse_source(mlbb.get_source(player_url))
            string = ''
            for line in stats:
                string += line + '\n'
        except mlbb.InvalidPlayerError:
            string = 'Invalid Player'

        self.label2 = tkinter.Label(self.window1, text=string, justify = 'left', font = 'TkFixedFont',
                                    padx = 5,pady = 5, background = '#89D8FA')
        self.label2.grid(row = 1, column = 0, columnspan = 6, sticky = tkinter.W + tkinter.E)        


Application()

