from pokedex.models import Teams
from django.test import TestCase

class TeamModelTests(TestCase):
    def test_team_creation(self):
        # Créer une équipe et vérifier ses attributs
        team = Teams.objects.create(
            name="Team Rocket",
            pokemon_1="meowth",
            pokemon_2="wobbuffet",
            pokemon_3="arbok",
            pokemon_4="weezing",
            pokemon_5="victreebel",
            pokemon_6="lickitung"
        )
        
        self.assertEqual(team.name, "Team Rocket")
        self.assertEqual(team.pokemon_1, "meowth")
        self.assertEqual(team.pokemon_6, "lickitung")
        
        # Vérifier la méthode __str__
        self.assertEqual(str(team), f"{team.id}, Team: Team Rocket")