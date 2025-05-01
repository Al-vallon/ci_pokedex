# SuperPokedex

## Description

SuperPokedex est une application web construite avec Django qui permet aux utilisateurs de parcourir, rechercher et consulter des informations détaillées sur différents Pokémon. L'application offre des fonctionnalités de filtrage par type, capacités et autres caractéristiques.

## Fonctionnalités principales

- Navigation dans la liste complète des Pokémon
- Filtrage par type, capacité et autres attributs
- Affichage détaillé des informations pour chaque Pokémon
- API RESTful pour accéder aux données Pokémon
- Déploiement simplifié via Docker

## Installation

### Prérequis

- Docker (version 20.10 ou supérieure)
- Docker Compose (recommandé)

### Option 1 : Utiliser l'image Docker prête à l'emploi

L'image Docker est automatiquement générée par notre pipeline CI et disponible sur GitHub Container Registry :

```bash
# Télécharger l'image
docker pull ghcr.io/al-vallon/ci_pokedex/superpokedex-web:latest

# Lancer le conteneur
docker run -p 8000:8000 ghcr.io/al-vallon/ci_pokedex/superpokedex-web:latest
```

### Option 2 : Installation locale

1. **Cloner le dépôt :**
   ```bash
   git clone https://github.com/Al-vallon/ci_pokedex.git
   cd ci_pokedex
   ```

2. **Construire et lancer le conteneur Docker :**
   ```bash
   # Avec Docker Compose
   docker-compose up --build
   
   # Ou directement avec Docker
   docker build -t superpokedex .
   docker run -p 8000:8000 superpokedex
   ```

3. **Accéder à l'application :**
   Une fois le conteneur lancé, ouvrez votre navigateur et accédez à [http://localhost:8000](http://localhost:8000)

4. **Appliquer les migrations (première utilisation) :**
   ```bash
   docker exec -it superpokedex python manage.py migrate
   ```

### Option 3 : Installer le package Python

Le package Python de SuperPokedex est généré par notre pipeline CI.

Pour plus d'informations sur l'accès et l'installation du package, consultez la [documentation CI](CI.md).

## Développement

### Structure du projet

```
superpokedex/
├── pokedex/          # Application Django principale
├── myproject/        # Configuration projet Django
├── tests/            # Tests unitaires et d'intégration
├── templates/        # Templates HTML
├── static/           # Fichiers statiques (CSS, JS, images)
├── manage.py         # Script de gestion Django
├── requirements.txt  # Dépendances Python
└── Dockerfile        # Instructions de construction du conteneur
```

### Tests

Le projet utilise pytest pour les tests unitaires et d'intégration. Pour exécuter les tests localement :

```bash
pip install -r requirements.txt
pytest
```

Les tests couvrent :
- Tests fonctionnels de l'API Pokémon
- Tests des modèles de données
- Tests d'intégration

## Intégration Continue

SuperPokedex utilise GitHub Actions pour l'intégration continue, avec les étapes suivantes :
- Vérification du style de code (lint) avec flake8
- Exécution des tests unitaires avec pytest
- Analyse de sécurité du code (CodeQL)
- Scan de vulnérabilités (Trivy)
- Génération du package Python
- Construction et publication de l'image Docker

Pour plus de détails sur le pipeline CI, consultez la [documentation CI complète](CI.md).

## Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.
