from django.test import TestCase, RequestFactory
from django.urls import reverse
from unittest.mock import patch, MagicMock
from pokedex.views import getAllPokemon
import json

class GetPokemonByIdTests(TestCase):
    @patch('pokedex.views.requests.get')
    def test_getPokemonById_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'id': 1,
            'name': 'bulbasaur',
            'sprites': {'front_default': 'https://example.com/sprite.png'},
            'types': [{'type': {'name': 'grass'}}],
            'abilities': [{'ability': {'name': 'overgrow'}}],
            'stats': [{'stat': {'name': 'hp'}, 'base_stat': 45}],
            'height': 7,
            'weight': 69
        }
        mock_get.return_value = mock_response
        
        response = self.client.get(reverse('getPokemonById', args=[1]))
        
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'pokemon.html')

        self.assertEqual(response.context['pokemon']['name'], 'bulbasaur')
    
    @patch('pokedex.views.requests.get')
    def test_getPokemonById_not_found(self, mock_get):

        mock_response = MagicMock()
        mock_response.status_code = 404

        response = self.client.get(reverse('getPokemonById', args=[999]))

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.content.decode(), "Pokémon not found")