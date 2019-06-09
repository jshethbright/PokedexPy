# COGS18 Final Project: Pokédex
## Description:
This is a python terminal version of the Pokédex from the popular Pokémon game series. The program connects to an API located at 'pokeapi.co/api/v2' which contains information on every Pokémon and then gets information specified by the user.

This program employs the concepts of utilizing APIs effectively as well as implements some text elements from chatbots and basic UI design.

This program can display various attributes of a Pokémon, here are some examples:
* Flavor Text
* Moves
* Abilities
* Types
* Information on any move, ability or type such as:
    * Power
    * Accuracy
    * Effect
* Much More!

## Process:
The program connects to an API for the Pokémon game series using the 'requests' module and returns JSON information from various endpoints. 

I first created the functions for getting all the overarching information from the PokeAPI that I needed, and then created other functions for getting specific information from the overarching information. An example of this would be 'get_species_info()' which gets the species info of a given Pokémon and 'get_evolution_chain()' which gets the evolution chain of from the given species info. This reduces the number of API calls and prevents rate limiting.

Additionally, there is also built in protection for nonstandard text inputs. The program gets the raw text input from a user then converts it to lowercase and also replaces spaces with dashes or underscores when needed. This allows a user to not worry about proper uppercases or lowercases and gracefully accepts nonstandard inputs such as 'pIKacHU' without erroring.

## Setup:
**While the program DOES work perfectly within this Jupyter notebook, it is highly recommended to run the program from 'my_script.py' in the scripts folder for better readability through 'colorama.' It is also recommended to use a black terminal that is maximized for readability**

**This program requires 'requests' and 'colorama'**


## Examples:
Here are some example **Pokémon** to test the program:
* Bulbasaur
* Charizard
* Dialga
* Rayquaza
* Furret

Here are some example **moves**:
* Hidden Power (Demonstrates the full extent of information handling/display of the program)
* Draco Meteor
* Quick Attack

Here are some example **abilities**:
* Overgrow
* Adaptability
* Static

Here are some example **types**:
* Flying
* Dragon
* Grass