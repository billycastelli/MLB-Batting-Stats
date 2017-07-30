#### MLB Stats
#      The information used here was obtained free of
#     charge from and is copyrighted by Retrosheet.  Interested
#     parties may contact Retrosheet at "www.retrosheet.org".

#### MLB Stats

#Stats provided by www.retrosheet.org

import MLB_stats_builder as mlbb

def inputName():
    name = input('Enter the name of an MLB player: ')
    return name

def getStats(player:str):
    print()
    last_name_url = mlbb.last_name_url(player)
    #print(last_name_url)
    last_name_source = mlbb.get_source(last_name_url)
    #print(last_name_source)
    #text_output = open('Output.txt','w')
    player_url = mlbb.get_player_url(player,last_name_source)
    #print(mlbb.get_source(player_url))
    stats = mlbb.parse_source(mlbb.get_source(player_url))
    for line in stats:
        print(line)

if __name__ == "__main__":
    name = inputName()
    getStats(name)
   
    
#put stats in dict so they are stored in the program for access

    
    
