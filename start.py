import os
import time
from settings import *
from menu import *
import random

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

def func_clear_console():
    os.system('clear')

def func_main_menu():
    while True:
        global is_exit;
        global new_game_menu;
        print("Welcome to Console City");
        print("Choose between a new game or to load a save");
        print("1. New Game");
        print("2. Load Game");
        print("3. Exit");
        user_input = input("")
        if user_input == "3":
            is_exit = "1";
            break
        elif user_input == "1":
            new_game_menu = "1";
            break
        elif user_input == "2":
            print("do other next");

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
    start_game = "1";
    new_game_menu = "0";

def func_load_game():
    print("Not implemented yet");

def func_start_game():
    global city_name
    global new_game_difficulty
    global var_day
    global var_people
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

def func_play_game():
    global city_name
    global new_game_difficulty
    global var_day
    global var_people
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
        print("Food: " + str(var_food));
        print("People: " + str(var_people));
        if list_building_builds[0] == 1:
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
                        list_building_builds[0] = 1;
                        list_building_builds[1] = 1;
                        list_building_builds[2] = 1;
                        list_building_builds[3] = list_farm_build_lvl1[2];
                        print("Build..");
                elif input_farm_choose == "2":
                    print("ok");
        elif input_play_choose == "resources":
            print("You have:")
            print(str(var_food) + " food.")
        elif input_play_choose == "next":
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
    
