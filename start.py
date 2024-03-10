import os
import time
from settings import *
from menu import *

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
    print("Lets play.");
    while True:
        print("Please choose from menu, if you need help, just write help.")
        print("You have:");
        print("Food: " + str(var_food));
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
        elif input_play_choose == "resources":
            print("You have:")
            print(str(var_food) + " food.")
        elif input_play_choose == "next":
            var_food = var_food - var_people;
            ##print("You got:")
            ##print(str(var_food) + " food.")
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
    
