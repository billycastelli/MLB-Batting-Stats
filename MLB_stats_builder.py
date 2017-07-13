# MLB Stats builder


import json
import urllib.parse
import urllib.request
import requests
import re


BASE_URL = 'http://www.retrosheet.org/boxesetc/'


class InvalidPlayerError(Exception):
    pass




def last_name_url(player:str):
    player = player.split()
    last_name = player[-1]
    #print(last_name)
    first2 = last_name[:2].upper()
    #print(first2)
    return BASE_URL + 'MISC/PLD_' + first2 + '.htm'


def get_source(url: str)->dict:
    response = None

    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        return json_text
    except:
        raise InvalidPlayerError

    finally:
        if response != None:
            response.close()


def check_if_player(player:str,source:str):
    if player.lower() not in source.lower():
        raise InvalidPlayerError
    else:
        print('Player found')



def get_player_url(player:str,source:str):
    check_if_player(player,source)
    source = source.split('</A>')
    for line in source:
        if player.lower() in line.lower():
            addThis = line[13:28]
            return BASE_URL + addThis



def parse_source(source):
    #use re to get rid of all html tags
    print()
    on = 0

    cleanSource = re.sub('<[^>]*>','',source)

    file = open("Stats.txt", 'w')
    file.write(cleanSource)
    file = open("Stats.txt", 'r')

    for line in file:
        if 'Batting Record' in line:
            on = 1
        if 'Total NL' in line:
            line = ''
        if 'Total AL' in line:
            line = ''

        if 'Total    (' in line:
            line = re.sub(r'([T][o][t][a][l][ ]{4})','Total',line)
            line = re.sub(r'([S][p][l][i][t][s])','',line.strip())
            line = re.sub(r'([Y][e][a][r][s])','yrs',line.strip())
            print(line)

            file.close()
            return
        if on and len(line)>0:
            line = re.sub(r'([D][a][i][l][y][ ][S][p][l][i][t][s])|([ ]{12})|([ ][S][p][l][i][t][s])','',line.strip())
            print(line)

           
