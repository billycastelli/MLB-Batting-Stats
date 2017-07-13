#### MLB Stats
#      The information used here was obtained free of
#     charge from and is copyrighted by Retrosheet.  Interested
#     parties may contact Retrosheet at "www.retrosheet.org".

import MLB_stats_builder as mlbb

def inputName():
    name = input('Enter the name of an MLB player: ')
    return name

def get_stats():
    print()
    player = inputName()
    last_name_url = mlbb.last_name_url(player)
    #print(last_name_url)
    last_name_source = mlbb.get_source(last_name_url)
    #print(last_name_source)
    #text_output = open('Output.txt','w')
    player_url = mlbb.get_player_url(player,last_name_source)
    #print(mlbb.get_source(player_url))
    stats = mlbb.parse_source(mlbb.get_source(player_url))

if __name__ == "__main__":
    while True:
        get_stats()
    

    
    
