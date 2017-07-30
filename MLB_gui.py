#tkinter


import tkinter
import MLB_stats_builder as mlbb



class Application:
    def __init__(self):
        self.window1 = tkinter.Tk()
        self.window1.title('Batting Stats Widget')
        #self.canvas = tkinter.Canvas(
#            master = self.window1, width = 250, height = 30)#, background = '#A6D0DE')
#        self.canvas.grid(row = 1, column = 0,
                #sticky = tkinter.N + tkinter.E + tkinter.S + tkinter.W)
        
        self.label = tkinter.Label(master=self.window1, text = "Enter the name of an MLB player:")
        self.label.grid(row = 0,column=0, sticky = tkinter.W)


        self.button = tkinter.Button(master= self.window1, text = 'Enter')
        self.button.grid(row = 0, column = 5, sticky = tkinter.E)
        self.button.bind('<Button-1>', self.get_player)

        self.textBox=tkinter.Entry(self.window1)
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
        player_url = mlbb.get_player_url(player,last_name_source)
        #print(mlbb.get_source(player_url))
        stats = mlbb.parse_source(mlbb.get_source(player_url))

        string = ''
        for line in stats:
            string += line + '\n'


    


        self.label2 = tkinter.Label(self.window1, text=string, justify = 'left', font = 'TkFixedFont',
                                    padx = 5,pady = 5, background = '#A6D0DE')
        self.label2.grid(row = 1, column = 0, columnspan = 6, sticky = tkinter.W)        


Application()

