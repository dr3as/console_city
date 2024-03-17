import os
import time
from settings import *
from menu import *
import random

##sette globals?
global is_exit
is_exit = "0";
global new_game_menu
new_game_menu = "0";
global city_name
city_name = "";
global start_game
start_game = "0";
global new_game_difficulty
new_game_difficulty = "";
global var_day
var_day = "0";
global var_wood
global var_stone
global var_people
global var_food
global list_builded_buildings
global play_game
play_game = "0";
global list_buildings
global list_building_builds
global var_workers
var_workers = 0;

##function for å tømme skjerm
def func_clear_console():
    os.system('clear')

##function for meny
def func_main_menu():
    while True:
        global is_exit;
        global new_game_menu;
        ##print meny
        print("Welcome to Console City");
        print("Choose between a new game or to load a save");
        print("1. New Game");
        print("2. Load Game");
        print("3. Exit");
        ##ta imot input
        user_input = input("")
        ##exit
        if user_input == "3":
            is_exit = "1";
            break
        ##lag nytt spill og sett variable for det
        elif user_input == "1":
            new_game_menu = "1";
            break
        ##load gammelt save
        elif user_input == "2":
            print("do other next");

##function for å lage nytt spill
def func_new_game():
    global city_name
    global start_game
    global new_game_menu
    global new_game_difficulty
    func_clear_console();
    print("Choose difficulty");
    print("1. Easy");
    print("2. Medium");
    print("3. Hard");
    ##Velge nivå
    input_difficulty = input("");
    if input_difficulty == "1":
        new_game_difficulty = "easy";
    elif input_difficulty == "2":
        new_game_difficulty = "medium";
    elif input_difficulty == "3":
        new_game_difficulty = "hard";
    func_clear_console();
    print("Nice, you like it " + new_game_difficulty);
    print("Please choose a name for your city:");
    input_city_name = input("")
    print(input_city_name + " it is")
    city_name = input_city_name;
    ##time.sleep(3)
    ## sette variabel for å sette spill og fjerne den for å lage nytt 
    start_game = "1";
    new_game_menu = "0";

#function for å loade spill
def func_load_game():
    print("Not implemented yet");

##function for å starte spill/spille
def func_start_game():
    global city_name
    global new_game_difficulty
    global var_day
    global var_people
    global var_workers
    global var_wood
    global var_stone
    global var_food
    global list_builded_buildings
    global play_game
    global start_game
    global new_game_menu

    func_clear_console();
    print(city_name + " is just founded.");
    print("The resources available is:")
    ##sett variabler basert på vasnkelighetsgrad
    if new_game_difficulty == "easy":
        print("Wood: " + str(easy_wood_start) + ".");
        var_wood = easy_wood_start;
        print("Stone: " + str(easy_stone_start) + ".");
        var_stone = easy_stone_start;
        print("People: " + str(easy_people_start) + ".");
        var_people = easy_people_start;
        print("Food: " + str(easy_food_start) + ".");
        var_food = easy_food_start;
    elif new_game_difficulty == "medium":
        print("Wood: " + str(medium_wood_start) + ".");
        var_wood = medium_wood_start;
        print("Stone: " + str(medium_stone_start) + ".");
        var_stone = medium_stone_start;
        print("People: " + str(medium_people_start) + ".");
        var_people = medium_people_start;
    elif new_game_difficulty == "hard":
        print("Wood: " + str(hard_wood_start) + ".");
        var_wood = hard_wood_start;
        print("Stone: " + str(hard_stone_start) + ".");
        var_stone = hard_stone_start;
        print("People: " + str(hard_people_start) + ".");
        var_people = hard_people_start;
    list_builded_buildings = ["0", "0", "0"]
    ##time.sleep(3)
    func_clear_console();
    new_game_menu = "0";
    start_game = "0";
    play_game = "1";

#function for selve spillingen

def func_play_game():
    global city_name
    global new_game_difficulty
    global var_day
    global var_people
    global var_workers
    global var_wood
    global var_stone
    global var_food
    global list_builded_buildings
    global play_game
    global start_game
    global new_game_menu
    global list_buildings
    global list_farm_build_lvl1
    global list_building_builds

    print("Lets play.");
    while True:
        print("Please choose from menu, if you need help, just write help.");
        print("You have:");
        print("People: " + str(var_people));
        print("Workers: " + str(var_workers));
        print("Food: " + str(var_food));
        print("Wood " + str(var_wood));
        print("Stone: " + str(var_stone));
        if list_buildings[0] == 0:
            print("Farm: No");
        elif list_buildings[0] >= 1:
            print("Farm: Level " + str(list_buildings[0]));
        print("Woodcutter: No");
        print("Stonecutter: Yes, Level 2, makes blabla new stone per day and have 2 worker");
        print("House: No, Chance of new pople is 5%");
        if list_building_builds[0] == 1:
            if list_building_builds[3] == 0:
                    if list_building_builds[3] == 0:
                        list_buildings[0] = list_buildings[0] + 1;
                        list_building_builds[0] = 0;
                        list_building_builds[1] = 0;
                        list_building_builds[2] = 0;
                        list_building_builds[3] = 0;
            if list_building_builds[1] == 1:
                print("You are building a Farm level " + str(list_building_builds[2]) + " and there are " + str(list_building_builds[3]) + " days left");
        input_play_choose = input("");
        if var_food <= 0:
            print("No food, people died")
            time.sleep(5);
            new_game_menu = "0";
            start_game = "0";
            play_game = "0";
            break;
        
        if input_play_choose == "exit":
            new_game_menu = "0";
            start_game = "0";
            play_game = "0";
            break;
        elif input_play_choose == "farm":
            print("Farm:");
            if list_buildings[0] == 0:
                print("You do not yet have a farm.");
                print("A farm level 1 cost " + str(list_farm_build_lvl1[0]) + " wood and " + str(list_farm_build_lvl1[1]) + " stone.");
                print("The farm have room for " + str(list_farm_build_lvl1[3]) + " worker and it takes " + str(list_farm_build_lvl1[2]) + " days to build.");
                print("It will produce " + str(list_farm_build_lvl1[4]) + " food each day");
                print("1. Build farm level 1.");
                print("2. Go back.");
                input_farm_choose = input("");
                if input_farm_choose == "1":
                    ##check if something else is being built
                    if list_building_builds[0] == 0:
                            if var_wood >= list_farm_build_lvl1[0]:
                                var_wood = var_wood - list_farm_build_lvl1[0];
                                if var_stone >= list_farm_build_lvl1[1]:
                                        var_stone = var_stone - list_farm_build_lvl1[1];
                                        if var_workers >= list_farm_build_lvl1[3]:
                                                var_workers = var_workers + list_farm_build_lvl1[3];
                                                var_people = var_people - list_farm_build_lvl1[3];
                                                list_building_builds[0] = 1;
                                                list_building_builds[1] = 1;
                                                list_building_builds[2] = 1;
                                                list_building_builds[3] = list_farm_build_lvl1[2];
                                                print("Starting to build");
                                                time.sleep(1);
                                                func_clear_console();
                    elif list_building_builds[0] == 1:
                        print("Something else is being built");
                        time.sleep(1);
                        func_clear_console();
                elif input_farm_choose == "2":
                    print("ok");
                    func_clear_console();
        elif input_play_choose == "resources":
            print("You have:")
            print(str(var_food) + " food.")
        elif input_play_choose == "next":
            if list_building_builds[0] == 1:
                if list_building_builds[3] > 0:
                    list_building_builds[3] = list_building_builds[3] - 1;
            var_new_food = 0;
            if list_buildings[0] == 1:
                var_new_food = var_new_food + list_farm_build_lvl1[4];
            var_food = var_food + var_new_food;
            var_food = var_food - var_people;
            var_wood = var_wood;
            var_stone = var_stone;
            var_is_born = random.randint(0,19);
            if var_is_born == 14:
                var_people = var_people + 1;
            func_clear_console();
            print("Everyone sleeps..");
            print("Z")
            time.sleep(1);
            func_clear_console();
            print("Everyone sleeps..");
            print("ZzZ")
            time.sleep(1);
            func_clear_console();
            print("Everyone sleeps..");
            print("ZzZzZ")
            time.sleep(1);
            func_clear_console();

while True:
    func_clear_console();
    if is_exit == "1":
        exit();
    elif new_game_menu == "1":
        func_new_game();
    elif start_game == "1":
        func_start_game();
    elif play_game == "1":
        func_play_game();
    else:
        func_main_menu();
    
