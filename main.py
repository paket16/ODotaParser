import requests
import json
from colorama import init, Fore, Back, Style

def console_picture():
    print(Style.BRIGHT + Fore.RED)
    print("⣶⣶⣶⣦⣶⣶⣶⣴⣶⣦⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⣿⣯⡉⠻⢿⣿⣿⣉⠉⣿⣿⡇⠀⠀⠀⠀⣤⠀⠠⢤⣄⠀⠀⠀⠀⢀⠤⠒⠲⢤⡀⠀⢠⡤⠄⣤⠠⠤⡆⠀⠀⠀⣤⠀⠀⠀⠀⠀⠀⠀⠀⠄⠒⢤⡀⠀")
    print("⢿⣿⣿⣄⠀⠉⠻⣿⣷⣿⣿⠁⠀⠀⠀⠀⣿⠀⠀⠀⠹⣧⠀⠀⢰⡏⠀⠀⠀⠀⣿⡆⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⡸⠹⣇⠀⠀⠀⠀⠀⠀⠈⠀⠀⢸⡇⠀")
    print("⣾⣿⢿⣿⣷⣄⠀⠀⠙⠻⣿⡄⠀⠀⠀⠀⣿⠀⠀⠀⢠⡟⠀⠀⠸⣷⠀⠀⠀⠀⣿⠃⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⢰⣃⣀⣻⣆⠀⠀⠀⠀⠀⠀⠀⡠⠋  ")
    print("⣾⣇⠀⢙⣿⣿⣷⣄⠀⢠⣿⡇⠀⠀⠀⠀⠛⠦⠤⠐⠋⠀⠀⠀⠈⠓⠦⠤⠚⠁⠀⠀⠀⠀ ⠛⠀⠀⠀ ⠄⠋⠀⠀⠈⠛⠠⠀⠀⠀⠀⠚⠒⠒⠊⠀")
    print("⠿⠿⠿⠿⢿⠿⡿⠿⠿⠿⠿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")

    print("\n", "\n")
    print(Style.BRIGHT + Fore.GREEN)
    print("Привет это простейший анализатор игры дота, выбери дейвствие: \n 1.\tПоказать пики и баны \n 2.\tСформировать отчёт о пиках и банах \n 0.\tВыход \n")
    print(Style.BRIGHT + Fore.WHITE)


def getResults(match_id):
    res = requests.get('https://api.opendota.com/api/matches/' + match_id)

    resDict = json.loads(res.text)

    return resDict

def getConstant(constant):
    res = requests.get("https://api.opendota.com/api/constants/"+constant)

    resDict = json.loads(res.text)

    return resDict

def showPickBans():
    picks_bans = resultsOfMatch["picks_bans"]

    for i in range(len(picks_bans)):
        if (picks_bans[i]['team']):
            team = 'Dire'

        else:

            team = 'Radiant'

        heroId = picks_bans[i]['hero_id'] - 1
        heroName = nameOfHeroes[list(nameOfHeroes.keys())[heroId]]['localized_name']

        if (picks_bans[i]['is_pick']):
            print(Style.BRIGHT + Fore.GREEN)
            action = "picks"

        else:
            print(Style.BRIGHT + Fore.RED)
            action = "bans"


        stringFinal = f"Team {team} {action} {heroName} "

        print(stringFinal)

        print(Style.BRIGHT + Fore.WHITE)

console_picture()

action = int(input())

if(action == 1):
    match_id = input("Введи id матча \t По умолчанию:'7423293270' \n")
    match_id = '7423293270' #тестовый матч

    resultsOfMatch = getResults(match_id)

    nameOfHeroes = getConstant("heroes")

    # обращение к элементу списка по индексу то есть в данном случае по айди героя
    # print(nameOfHeroes[list(nameOfHeroes.keys())[0]]['localized_name'])

    showPickBans()

elif(action == 2):
    print("Данная функция ещё в разработке")


elif(action == 0):
    exit(0)
