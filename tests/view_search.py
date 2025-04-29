from django.test import TestCase, RequestFactory
from django.urls import reverse
from unittest.mock import patch, MagicMock
from pokedex.views import getAllPokemon
import json

class SearchPokemonTests(TestCase):
    @patch('pokedex.views.requests.get')
    def test_searchPokemon_found(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'results': [
                {'name': 'bulbasaur', 'url': 'https://pokeapi.co/api/v2/pokemon/1/'},
                {'name': 'ivysaur', 'url': 'https://pokeapi.co/api/v2/pokemon/2/'}
            ]
        }

        mock_pokemon_response = MagicMock()
        mock_pokemon_response.status_code = 200
        mock_pokemon_response.json.return_value = {
            'name': 'bulbasaur',
            'sprites': {'front_default': 'https://example.com/sprite.png'}
        }

        mock_get.side_effect = [mock_response, mock_pokemon_response]

        response = self.client.get(reverse('search_pokemon'), {'pokemon-name': 'bulba'})

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'pokedex.html')

        self.assertEqual(len(response.context['all_pokemons']), 1)
        self.assertEqual(response.context['all_pokemons'][0]['name'], 'bulbasaur')
    
    def test_searchPokemon_empty_name(self):
        response = self.client.get(reverse('search_pokemon'), {'pokemon-name': ''})
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content.decode(), "Pokémon name is required")