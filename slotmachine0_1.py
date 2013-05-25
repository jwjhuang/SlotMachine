# Source File Name: slotmachine.py
# Author's Name: Aldrin Jerome Almacin
# Last Modified By: Aldrin Jerome Almacin
# Date Last Modified: Saturday May 25, 2013
"""
  Program Description:  This program simulates a Casino-Style Slot Machine. It provides an GUI
                        for the user that is an image of a slot machine with Label and Button objects
                        created through the tkinter module
"""

# import statements
import random
from Tkinter import *

def main():
  slot_machine = SlotMachine(500, 1000)
  slot_machine.start_game()

class SlotMachine:
  def __init__(self, starting_jackpot, starting_cash):
    self.POSSIBLE_BETS = "10, 20, 50, 100"
    self.JACKPOT_INCREASE_RATE = .15

    self.starting_jackpot = starting_jackpot
    self.starting_cash = starting_cash

    self.set_initial_values()

  def set_initial_values(self):
    self.current_jackpot = self.starting_jackpot
    self.current_cash = self.starting_cash
    self.results = 3*[""]
    self.turns = 0
    self.bet = 10
    self.wins = 0
    self.loses = 0

  def start_game(self):
    # Start the game Loop
    continue_playing = True
    while (continue_playing):
      print("This is Aldrin's Slot Machine")
      print("What do you want to do?")
      print("1: Set Bet")
      print("2: Spin")
      print("3: Reset")
      print("4: Quit")
      selection = raw_input(">>> ")

      if (selection == "1"):
        self.set_bet()
      elif (selection == "2"):
        self.spin()
      elif (selection == "3"):
        self.reset()
      elif (selection == "4"):
        continue_playing = False
      else:
        print("Invalid Value entered")

  def set_bet(self):
    bet = -1
    while True:
      print("How much would you bet?")
      print self.POSSIBLE_BETS
      bet = raw_input(">>> ")
      if (bet in self.POSSIBLE_BETS.split(", ")):
        break
      else:
        print("Invalid bet value!")
    self.bet = int(bet)

  def spin(self):
    self.__pay()
    self.__increase_jackpot()

    for spin in range(3):
      spinned_result = random.randint(0, 100)

      if spinned_result in range(0, 40):
          self.results[spin] = "Blank"
      elif spinned_result in range(40, 56):
          self.results[spin] = "Grapes"
      elif spinned_result in range(56, 70):
          self.results[spin] = "Banana"
      elif spinned_result in range(70, 82):
          self.results[spin] = "Orange"
      elif spinned_result in range(82, 89):
          self.results[spin] = "Cherry"
      elif spinned_result in range(89, 95):
          self.results[spin] = "Bar"
      elif spinned_result in range(95, 99):
          self.results[spin] = "Bell"
      elif spinned_result in range(99, 100):
          self.results[spin] = "Seven"

    self.__check_results()

  def __pay(self):
    self.current_cash -= self.bet

  def __increase_jackpot(self):
    self.current_jackpot += (int(self.bet * self.JACKPOT_INCREASE_RATE))

  def __check_results(self):
    print self.results

  def reset(self):
    self.set_initial_values()

class Player:
  def __init__(self, name):
    self.name = name

  def get_name(self):
    return self.name

if __name__ == "__main__": main()
