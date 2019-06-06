import requests

from colorama import init, Fore, Style

'''
Initializes colorama and sets variables for colors for ease of use

'''

init(autoreset = True)

RED = Fore.RED
GREEN = Fore.GREEN
BLUE = Fore.BLUE
YELLOW = Fore.YELLOW
CYAN = Fore.CYAN
MAGENTA = Fore.MAGENTA
RESET = Style.RESET_ALL

url = 'https://pokeapi.co/api/v2/'

class pokeApi():
    """
    Suite of functions querying the PokeApi
    """
    def __init__(self, api_url = 'https://pokeapi.co/api/v2/'):
        """
        Input: string
        
        Initializes the pokeApi object with a given url, which can be changed as the API url might change"""
        self.api_url = api_url
        chosen_pokemon = None
    
    def get_pokemon_info(self, pokemon):
        """
        Input: string
        Output: JSON dict
        
        Gets information in JSON format of a given pokemon
        """
        request = requests.get(self.api_url + 'pokemon/' + pokemon)
        return request.json()
    
    def get_species_info(self, chosen_pokemon_info):
        """
        Input: JSON dict
        Output: JSON dict
        
        Gets the species information of a pokemon from its JSON info by creating a request
        from a species url contained within the input JSON dict 
        """
        species_url = chosen_pokemon_info['species']['url']
        species_request = requests.get(species_url)
        species = species_request.json()
        return species
    
    def get_name(self, chosen_pokemon_info):
        """
        Input: JSON dict
        Output: string
        
        Gets the name of a given pokemon from its JSON info
        """
        name = chosen_pokemon_info['name']
        return name
    
    def get_type(self, chosen_pokemon_info):
        """
        Input: JSON dict
        Output: list
        
        Gets the types of a given pokemon from its JSON info
        """
        i = 0
        output = []
        types = chosen_pokemon_info['types']
        while i < len(types):
            output.append(types[i]['type']['name'].capitalize())
            i += 1
        return output
    
    def get_moves(self, chosen_pokemon_info):
        """
        Input: JSON dict
        Output: list
        
        Gets the possible moves of a given pokemon from its JSON info
        """
        moves = chosen_pokemon_info['moves']
        i = 0
        output = []
        while i < len(moves):
            output.append(moves[i]['move']['name'].replace('-', ' ').title())
            i += 1
        return output
    
    def get_weight(self, chosen_pokemon_info):
        """
        Input: JSON dict
        Output: integer
        
        Gets the weight of a given pokemon from its JSON info
        """
        weight = chosen_pokemon_info['weight']
        return weight
    
    def get_forms(self, chosen_pokemon_info):
        """
        Input: JSON dict
        Output: list
        
        Gets the forms of a given pokemon from its JSON info
        (This function was created but not used)
        """
        forms = chosen_pokemon_info['forms']
        i = 0
        output = []
        while i < len(forms):
            output.append(forms[i]['name'])
            i += 1
        return output
    
    def get_abilities(self, chosen_pokemon_info):
        """
        Input: JSON dict
        Output: list
        
        Gets the abilities of a given pokemon from its JSON info
        """
        abilities = chosen_pokemon_info['abilities']
        output = []
        i = 0
        while i < len(abilities):
            output.append(abilities[i]['ability']['name'].replace('-', ' ').title())
            i += 1
        return output
    
    def get_base_stats(self, chosen_pokemon_info):
        """
        Input: JSON dict
        Output: dictionary
        
        Gets the base stats of a given pokemon from its JSON info
        """
        base_stats = chosen_pokemon_info['stats']
        i = 0
        output = {}
        while i < len(base_stats):
            output[base_stats[i]['stat']['name'].replace('-', ' ').title().replace('Hp', 'HP')] = base_stats[i]['base_stat']
            i += 1
        return output
    
    def get_flavortext(self, species_info):
        """
        Input: JSON dict
        Output: string
        
        Gets the english flavor text of a given species of pokemon from its JSON info
        """
        species = species_info
        flavor_text_entries = species['flavor_text_entries']
        lang_is_english = False
        flavortext = None
        i = 0
        while not lang_is_english:
            if flavor_text_entries[i]['language']['name'] == 'en':
                flavortext = flavor_text_entries[i]['flavor_text']
                break
            else:
                i += 1
                if i == len(flavor_text_entries):
                    break
        
        return flavortext
    
    def get_evolution_chain(self, species_info):
        """
        Input: JSON dict
        Output: list
        
        Gets the evolution chain of a given species of pokemon from its JSON info
        """
        evolution_chain_url = species_info['evolution_chain']['url']
        evolution_chain_request = requests.get(evolution_chain_url)
        evolution_chain_info = evolution_chain_request.json()
        output = []
        output.append(evolution_chain_info['chain']['species']['name'].capitalize())
        i = 0
        j = 0
        while i < len(evolution_chain_info['chain']['evolves_to']):
            output.append(evolution_chain_info['chain']['evolves_to'][i]['species']['name'].capitalize())
            
            while j < len(evolution_chain_info['chain']['evolves_to'][i]['evolves_to']):
                output.append(evolution_chain_info['chain']['evolves_to'][i]['evolves_to'][j]['species']['name'].capitalize())
                j += 1
    
            i += 1
        
        if len(output) == 1:
            output = ['No Evolutions']
        
        return output
    
    def get_type_info(self, pokemon_type):
        """
        Input: string
        Output: JSON dict
        
        Gets the information (in JSON dict form) of a given input pokemon type
        """
        request = requests.get(self.api_url + 'type/' + pokemon_type)
        type_info = request.json()
        return type_info
    
    def get_ability_info(self, ability):
        """
        Input: string
        Output: JSON dict
        
        Gets the information (in JSON dict form) of a given input pokemon ability
        """
        request = requests.get(self.api_url + 'ability/' + ability)
        ability_info = request.json()
        return ability_info
    
    def get_move_info(self, move):
        """
        Input: string
        Output: JSON dict
        
        Gets the information (in JSON dict form) of a given input pokemon move
        """
        request = requests.get(self.api_url + 'move/' + move)
        move_info = request.json()
        return move_info      
    
    def get_ability_effect(self, ability_info):
        """
        Input: JSON dict
        Output: string
        
        Gets the english effect of a particular ability given its ability info
        """
        effect_entries = ability_info['effect_entries']
        effect = None
        i = 0
        while i < len(effect_entries):
            if effect_entries[i]['language']['name'] == 'en':
                effect = effect_entries[i]['effect']
                break
            i += 1
        return effect
    
  
    
class moveInfo():
    """
    Organizes JSON move information, such as power, accuracy, or priority, into class object 'moveInfo'
    """
    def __init__(self, move_info):
        self.name = move_info['name'].title().replace('-', ' ')
        self.accuracy = move_info['accuracy']
        self.effect_chance = move_info['effect_chance']
        self.power = move_info['power']
        self.pp = move_info['pp']
        self.priority = move_info['priority']
        self.damage_class = move_info['damage_class']['name'].title()
        i = 0
        while i < len(move_info['effect_entries']):
            if move_info['effect_entries'][i]['language']['name'] == 'en':
                self.effect = move_info['effect_entries'][i]['effect'].replace('$effect_chance', str(self.effect_chance))
                break
            i += 1
            
        self.flavortext = None
        i = 0
        while i < len(move_info['flavor_text_entries']):
            if move_info['flavor_text_entries'][i]['language']['name'] == 'en':
                self.flavortext = move_info['flavor_text_entries'][i]['flavor_text']
                break
            i += 1

        if self.power == None:
            self.power = 'N/A'
        
        if self.accuracy == None:
            self.accuracy = 'N/A'
    

class typeInfo():
    """
    Organizes JSON type damage information into class object 'typeInfo'
    """
    def __init__(self, type_info):
        self.name = type_info['name'].capitalize()
        double_damage_from = type_info['damage_relations']['double_damage_from']
        self.double_damage_from = []
        i = 0
        while i < len(double_damage_from):
            self.double_damage_from.append(double_damage_from[i]['name'].capitalize())
            i += 1
            
        double_damage_to = type_info['damage_relations']['double_damage_to']
        self.double_damage_to = []
        j = 0
        while j < len(double_damage_to):
            self.double_damage_to.append(double_damage_to[j]['name'].capitalize())
            j += 1
            
        half_damage_from = type_info['damage_relations']['half_damage_from']
        self.half_damage_from = []    
        k = 0
        while k < len(half_damage_from):
            self.half_damage_from.append(half_damage_from[k]['name'].capitalize())
            k += 1
            
        half_damage_to = type_info['damage_relations']['half_damage_to']
        self.half_damage_to = []
        l = 0
        while l < len(half_damage_to):
            self.half_damage_to.append(half_damage_to[l]['name'].capitalize())
            l += 1
            
        no_damage_from = type_info['damage_relations']['no_damage_from']
        self.no_damage_from = []
        m = 0
        while m < len(no_damage_from):
            self.no_damage_from.append(no_damage_from[m]['name'].capitalize())
            m += 1
                
        no_damage_to = type_info['damage_relations']['no_damage_to']
        self.no_damage_to = []
        n = 0
        while n < len(no_damage_to):
            self.no_damage_to.append(no_damage_to[n]['name'].capitalize())
            n += 1
        
        if self.double_damage_from == []:
            self.double_damage_from = ['N/A']
        
        if self.double_damage_to == []:
            self.double_damage_to = ['N/A']
            
        if self.half_damage_from == []:
            self.half_damage_from = ['N/A']
            
        if self.half_damage_to == []:
            self.half_damage_to = ['N/A']
        
        if self.no_damage_from == []:
            self.no_damage_from = ['N/A']
        
        if self.no_damage_to == []:
            self.no_damage_to = ['N/A']

class abilityInfo():
    """
    Organizes JSON ability information into class object 'abilityInfo'
    """
    def __init__(self, ability_info):
        api = pokeApi()
        self.name = ability_info['name'].title().replace('-', ' ')
        self.effect = api.get_ability_effect(ability_info)


def Print_Pokemon_Info(chosen_pokemon_info, species_info):
    """
    Input: JSON dict, JSON dict
    Output: prints information
    
    Prints information about a specifed pokemon given its JSON pokemon info and
    its JSON species info
    """
    api = pokeApi()
    
    pokemon_name = api.get_name(chosen_pokemon_info)
    pokemon_base_stats = api.get_base_stats(chosen_pokemon_info)
    pokemon_evolution_chain = api.get_evolution_chain(species_info)
    pokemon_types = api.get_type(chosen_pokemon_info)
    pokemon_abilities = api.get_abilities(chosen_pokemon_info)
    pokemon_moves = api.get_moves(chosen_pokemon_info)
    pokemon_weight = api.get_weight(chosen_pokemon_info)
    pokemon_flavortext = api.get_flavortext(species_info)
    
    print('\nHere is ' + CYAN + pokemon_name.capitalize() + '\'s ' + RESET + 'information: \n' )
    
    print(CYAN + 'Evolution Chain:', ', '.join(pokemon_evolution_chain), '\n')
    
    print(CYAN + 'Base Stats:\n\n    ' , ', '.join("{}: {}".format(key, value) for key, value in pokemon_base_stats.items()), '\n')
    
    print(CYAN + 'Types:', ', '.join(pokemon_types), '\n')
    
    print(CYAN + 'Abilities:', ', '.join(pokemon_abilities), '\n')
    
    print(CYAN + 'Possible Moves:', ', '.join(pokemon_moves), '\n')
    
    print(CYAN + 'Weight:', pokemon_weight, '\n')
    
    print(CYAN + 'Flavor Text:', pokemon_flavortext, '\n')

def Print_Type_Info(typeInfo):
    """
    Input: class object
    Output: prints information
    
    Prints information about a specifed type given its typeInfo object
    """
    print('Your chosen type is: ' + CYAN + typeInfo.name + '\n')
    
    print(RED + 'Double Damage From:', ', '.join(typeInfo.double_damage_from))
    print(RED + 'Double Damage To:', ', '.join(typeInfo.double_damage_to), '\n')
    
    print(CYAN + 'Half Damage From:', ', '.join(typeInfo.half_damage_from))
    print(CYAN + 'Half Damage To:', ', '.join(typeInfo.half_damage_to), '\n')
    
    print(GREEN + 'No Damage From:', ', '.join(typeInfo.no_damage_from))
    print(GREEN + 'No Damage To:', ', '.join(typeInfo.no_damage_to), '\n')

def Print_Move_Info(moveInfo):
    """
    Input: class object
    Output: prints information
    
    Prints information about a specifed move given its moveInfo object
    """
    print('\nYour chosen move is: ' + CYAN + moveInfo.name + '\n')
    
    print(GREEN + 'Accuracy:', moveInfo.accuracy)
    print(CYAN + 'Effect Chance:', moveInfo.effect_chance)
    print(RED + 'Power:', moveInfo.power)
    print(CYAN + 'PP:', moveInfo.pp)
    print(YELLOW + 'Priority:', moveInfo.priority, '\n')
    print(CYAN + 'Damage Class:', moveInfo.damage_class, '\n')
    print(RED + 'Effect:', moveInfo.effect, '\n')
    print(CYAN + 'Flavor Text:', moveInfo.flavortext, '\n')

def Print_Ability_Info(abilityInfo):
    """
    Input: class object
    Output: prints information
    
    Prints information about a specifed abilty given its abilityInfo object

    """
    print('\nYour chosen ability is: ' + CYAN + abilityInfo.name + '\n')
    print(RED + 'Effect:', abilityInfo.effect, '\n')

        
def Pokedex(second_time = False):
    """
    Queries the user to enter a specific pokemon. The function then checks if the
    pokemon is valid. If yes, the function prints the information. If no, the function
    queries the user to enter a valid pokemon. After the information of a valid pokemon
    is printed, the function calls Know_More() to query the user for more info.
    
    If 'second_time' is True, meaning this is the second time the function has been called,
    the function will not display intro text
    """
    api = pokeApi()
    pokemon_is_valid = False
    use_intro_text = True
    IntroText = """
Welcome to the Python Pokédex! This program will
provide you with information about all Pokémon from
the game series. To get started, please pick a Pokémon
such as Pikachu or Eevee:\n
"""
    
    while not pokemon_is_valid:
        try:
            if use_intro_text and not second_time:
                raw_chosen_pokemon = input(IntroText)
            elif second_time:
                text = 'Choose Another Pokémon:\n'
                raw_chosen_pokemon = input(text)
            else:
                raw_chosen_pokemon = input()
            chosen_pokemon = raw_chosen_pokemon.lower()
            chosen_pokemon_info = api.get_pokemon_info(chosen_pokemon)
            pokemon_is_valid = True
        except:
            print("No Pokémon with that name was found! Please check your spelling and try again:\n")
            use_intro_text = False
            second_time = False
            pokemon_is_valid = False
        
        
    pokemon_name = api.get_name(chosen_pokemon_info)
    
    species_info = api.get_species_info(chosen_pokemon_info)
    
    #chose_text = '\nYour chosen Pokémon is: ' + pokemon_name.capitalize() + '\n'
    
    #print(chose_text)
    
    Print_Pokemon_Info(chosen_pokemon_info, species_info)
    
    Know_More()

def Know_More():
    """
    Continuation of the Pokedex() program. Queries the user if they want to know more about a
    'type,' 'ability,' 'move,' or another 'pokemon,' or exits the program. After choosing an
    option, the user enters a specific 'type,' 'ability,' 'move,' or  'pokemon.' The function
    checks if the input is valid and if a 'type,' 'ability,' 'move,' or  'pokemon' exists with
    that name. If yes, then the function prints the information. If not, the function queries the
    user to enter a valid 'type,' 'ability,' 'move,' or  'pokemon.'
    
    """
    
    api = pokeApi()
    next_text = """
What would you like to know more about? 
You can enter 'type,' 'ability,' or 'move' to learn more. 
Or enter 'Pokemon' to choose another Pokémon.
You can also enter 'Exit' to end the program\n
"""
    
    next_input = input(next_text).lower().replace(' ', '')
    if next_input == 'type':
        type_text = 'What type would you like to know more about?\n\n'
        
        type_is_valid = False
        use_type_text = True
        while not type_is_valid:
            try:
                if use_type_text:
                    type_input = input(type_text).lower().replace(' ', '')
                else:
                    type_input = input().lower().replace(' ', '')
                chosen_type = type_input
                chosen_type_info = api.get_type_info(chosen_type)
                type_is_valid = True
            except:
                print("No type with that name was found! Please check your spelling and try again:\n")
                use_type_text = False
                type_is_valid = False
            
        Type = typeInfo(chosen_type_info)
        Print_Type_Info(Type)
        
        Know_More()
        
    elif next_input == 'ability':
        ability_text = 'What ability would you like to know more about?\n'
        ability_is_valid = False
        use_ability_text = True
        while not ability_is_valid:
            try:
                if use_ability_text:
                    ability_input = input(ability_text).lower().replace(' ', '-')
                else:
                    ability_input = input().lower().replace(' ', '-')
                chosen_ability = ability_input
                chosen_ability_info = api.get_ability_info(chosen_ability)
                ability_info = abilityInfo(chosen_ability_info)
                ability_is_valid = True
            except:
                print("No ability with that name was found! Please check your spelling and try again:\n")
                use_ability_text = False
                ability_is_valid = False
        Print_Ability_Info(ability_info)
        Know_More()
        
    elif next_input == 'move':
        move_text = 'What move would you like to know more about?\n'
        move_is_valid = False
        use_move_text = True
        while not move_is_valid:
            try:
                if use_move_text:
                    move_input = input(move_text).lower().replace(' ', '-')
                else:
                    move_input = input().lower().replace(' ', '-')
                chosen_move = move_input
                chosen_move_info = api.get_move_info(chosen_move)
                move_info = moveInfo(chosen_move_info)
                move_is_valid = True
            except:
                print("No move with that name was found! Please check your spelling and try again:\n")
                use_move_text = False
                move_is_valid = False
                
        Print_Move_Info(move_info)
        Know_More()
    elif next_input == 'pokemon':
        Pokedex(True)
    elif next_input == 'exit':
        next
    else:
        print('\nInvalid input, please try again')
        Know_More()
        
    
    