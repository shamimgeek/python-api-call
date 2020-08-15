#!/usr/bin/env python3

import requests
from random import choice
from pyfiglet import figlet_format
from termcolor import colored

header = colored(figlet_format("Welcome to JOKE World!"), color='cyan')
print(header)


user_input = input("What would you like to search? ")

url = "https://icanhazdadjoke.com/search"

res = requests.get(
  url,
  headers={"Accept": "application/json"},
  params={"term": user_input}
).json()

num_jokes = res["total_jokes"]
results = res["results"]

if num_jokes > 1:
  print(colored(f"I found {num_jokes} about {user_input}. Here's one:", color='blue'))
  print(colored(choice(results)["joke"], color='blue'))
  
elif num_jokes == 1:
  print(colored(f"I found one joke about {user_input}",color='blue'))
  print(colored(results[0]["joke"], color='blue'))
else:
  print(colored(f"Sorry, couldn't find a joke with your term: {user_input}", color='red'))