from functions import pokeApi, moveInfo, typeInfo, abilityInfo

def test_pokemon():
    '''
    Asserts if API and functions work and info is valid by getting the information of a pokemon 'Bulbasaur' and checking if
    the name, types, weight, and evolution chain are valid and as expected 
    '''
    pokemon_test = pokeApi().get_pokemon_info('bulbasaur')
    species_test = pokeApi().get_species_info(pokemon_test)

    assert pokeApi().get_name(pokemon_test).title() == 'Bulbasaur'
    assert pokeApi().get_type(pokemon_test) == ['Poison', 'Grass']
    assert pokeApi().get_weight(pokemon_test) == 69
    assert pokeApi().get_abilities(pokemon_test) == ['Chlorophyll', 'Overgrow']
    assert pokeApi().get_evolution_chain(species_test) == ['Bulbasaur', 'Ivysaur', 'Venusaur']

def test_type():
    '''
    Asserts if API and functions work and info is valid by getting the information of a type 
    and determines if it is valid and expected
    '''
    type_test = pokeApi().get_type_info('poison')
    
    assert typeInfo(type_test).name == 'Poison'
    assert typeInfo(type_test).double_damage_to == ['Grass', 'Fairy']

def test_ability():
    '''
    Asserts if API and functions work and info is valid by getting the information of a ability 
    and determines if it is valid and expected
    '''
    ability_test = pokeApi().get_ability_info('overgrow')
    
    assert abilityInfo(ability_test).name == 'Overgrow'
    assert abilityInfo(ability_test).effect == 'When this Pokémon has 1/3 or less of its HP remaining, its grass-type moves inflict 1.5× as much regular damage.'

def test_move():
    '''
    Asserts if API and functions work and info is valid by getting the information of a move 
    and determines if it is valid and expected
    '''
    move_test = pokeApi().get_move_info('quick-attack')
    
    assert moveInfo(move_test).name == 'Quick Attack'
    assert moveInfo(move_test).accuracy == 100
    assert moveInfo(move_test).effect_chance == None
    assert moveInfo(move_test).damage_class == 'Physical'    