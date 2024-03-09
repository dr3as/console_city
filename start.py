import os
import time
from settings import *

global is_exit
is_exit = "0";
global new_game_menu
new_game_menu = "0";
global city_name
city_name = "";

def clear_console():
    os.system('clear')

def main_menu():
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

def new_game():
    global city_name
    clear_console();
    print("Choose difficulty");
    print("1. Easy");
    print("2. Medium");
    print("3. Hard");
    input_difficulty = input("");
    if input_difficulty == "1":
        new_game_difficulty = "easy";
    elif input_difficulty == "2":
        new_game_difficulty = "easy";
    elif input_difficulty == "3":
        new_game_difficulty = "easy";
    clear_console();
    print("Nice, you like it " + new_game_difficulty);
    print("Please choose a name for your city:");
    input_city_name = input("")
    print(input_city_name + " it is")
    city_name = input_city_name;

def load_game():
    print("Not implemented yet");

while True:
    clear_console();
    main_menu();
    if is_exit == "1":
        exit();
    if new_game_menu == "1":
        new_game();
