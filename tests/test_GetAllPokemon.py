from django.test import TestCase, RequestFactory#type: ignore
from django.urls import reverse  #type: ignore
from unittest.mock import patch, MagicMock
from pokedex.views import getAllPokemon

class GetAllPokemonTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
    
    @patch('pokedex.views.requests.get')
    def test_getAllPokemon_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'results': [
                {'name': 'bulbasaur', 'url': 'https://pokeapi.co/api/v2/pokemon/1/'},
                {'name': 'ivysaur', 'url': 'https://pokeapi.co/api/v2/pokemon/2/'}
            ],
            'next': 'https://pokeapi.co/api/v2/pokemon?offset=20&limit=20',
            'previous': None
        }
        mock_get.return_value = mock_response  
        mock_pokemon_response = MagicMock()
        mock_pokemon_response.status_code = 200
        mock_pokemon_response.json.return_value = {
            'name': 'bulbasaur',
            'sprites': {'front_default': 'https://example.com/sprite.png'}
        }
        
        mock_get.side_effect = [mock_response, mock_pokemon_response, mock_pokemon_response]
        
        request = self.factory.get(reverse('getAllPokemon'))
        response = getAllPokemon(request)
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed('pokedex.html')
    
    @patch('pokedex.views.requests.get')
    def test_getAllPokemon_api_error(self, mock_get):
        mock_get.side_effect = Exception("API Error")
        
        request = self.factory.get(reverse('getAllPokemon'))
        response = getAllPokemon(request)
        
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.content.decode(), "Pokémons not found")