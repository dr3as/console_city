import os
from settings import *
global is_exit
is_exit = "0";
global new_game_menu
new_game_menu = "0";

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
    clear_console();
    print("Choose difficulty");
    print("1. Easy");
    print("2. Medium");
    print("3. Hard");
    difficulty = input("");

def load_game():
    print("Not implemented yet");

while True:
    clear_console();
    main_menu();
    if is_exit == "1":
        exit();
    if new_game_menu == "1":
        new_game();




    

##first_menu = input("");
##def clear_console():
##    os.system('clear')
##clear_console();
##
##if first_menu == "1":
##    print("Choose difficulty");
##    print("1. Easy");
##    print("2. Medium");
##    print("3. Hard");
##    difficulty = input("");
##    def clear_console():
##        os.system('clear')
##
##   clear_console();
##elif first_menu == "2":
##    print("Choose what game to load");
##    print("1. lala");
##    print("2. lolo");
##    print("3. lulu");
##    difficulty = input("");
##    def clear_console():
##        os.system('clear')
##
##    clear_console();
##else:
##    print("Welcome to Console City");
##    print("Choose between a new game or to load a save");
##    print("1. New Game");
##    print("2. Load Game");
##    first_menu = input("");
##    def clear_console():
##        os.system('clear')
##    clear_console();