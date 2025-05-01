# Documentation de la CI Pipeline 

## Objectif général

Cette pipeline GitHub Actions a été mise en place pour assurer une qualité constante du code dans le projet SuperPokedex. Elle permet d’automatiser plusieurs étapes essentielles du cycle de développement : vérification du style de code, exécution des tests, analyse de sécurité et génération des artefacts nécessaires au déploiement. Grâce à cette intégration continue, chaque modification poussée sur la branche main est automatiquement analysée, testée, et validée.


## Vérification de la qualité du code (Lint)

La première étape de la pipeline consiste à vérifier la conformité du code Python grâce à l'outil flake8. Ce dernier permet de s'assurer que le code respecte les conventions PEP8 et ne contient pas d'erreurs évidentes comme des imports inutilisés ou des variables non utilisées.

Dans ce projet, la configuration de flake8 est centralisée dans un fichier setup.cfg, ce qui permet d’uniformiser les règles de style appliquées à tout le code source. Cela évite les divergences entre développeurs et garantit un code propre et lisible à long terme.


## Exécution des tests unitaires

Après le lint, la pipeline passe à l'exécution des tests unitaires à l'aide de pytest. Les tests sont organisés dans un fichier test.py (ou plusieurs fichiers de test si le projet évolue), qui contient les cas de test permettant de vérifier le bon fonctionnement des fonctions critiques de l'application.

Les tests unitaires mis en place couvrent plusieurs aspects essentiels de l'application :

**Tests fonctionnels de l'API Pokémon** :
- Validation des endpoints principaux (/api/pokemon/, /api/types/, etc.)
- Vérification de la récupération correcte des données de Pokémon individuels
- Tests de pagination et de filtrage des résultats

**Tests de modèles de données** :
- Vérification que les objets Pokémon sont correctement instanciés
- Validation des conversions entre formats (JSON/objets Python)
- Tests des relations entre modèles (par exemple, Pokémon et ses types associés)

**Tests d'intégration** :
- Validation du flux complet de recherche de Pokémon
- Vérification des interactions avec la base de données
- Tests de mise en cache des requêtes fréquentes

La couverture de code est également mesurée pendant l'exécution des tests via le plugin pytest-cov, permettant de s'assurer que la majorité du code est effectivement testée.

Les dépendances nécessaires sont installées depuis le fichier requirements.txt, puis pytest est lancé pour valider automatiquement les comportements attendus. Si un test échoue, la pipeline s'arrête immédiatement, ce qui permet de détecter rapidement les régressions introduites par une modification du code.


## Analyse de sécurité statique (CodeQL)

Une fois les tests passés, une analyse de sécurité est réalisée via CodeQL, l’outil officiel de GitHub pour l’analyse statique. Cette étape inspecte le code source Python à la recherche de vulnérabilités potentielles telles que des injections, des fuites d’informations, ou des pratiques risquées.

CodeQL permet de détecter des failles dès l’étape de développement, avant même qu'elles ne soient exposées en production. C’est une couche de sécurité essentielle pour les projets qui manipulent des données utilisateurs ou interagissent avec des services externes.


## Scan de vulnérabilités (Trivy)

En parallèle de l’analyse statique, la pipeline effectue un scan de l’image Docker avec l’outil Trivy. Ce scan couvre deux types de vulnérabilités : celles liées au système d’exploitation (comme les paquets système obsolètes) et celles des bibliothèques Python incluses dans l’image.

Trivy signale les failles classées HIGH ou CRITICAL pour permettre aux développeurs de corriger immédiatement les versions concernées. Cela garantit que les images Docker produites sont sécurisées et prêtes à être utilisées en production.


## Génération du package Python

Une fois les tests validés et le scan Trivy terminé, la pipeline procède à la construction du package Python. Le projet est packagé en utilisant le module build, qui génère un fichier .whl (wheel), un format standardisé pour la distribution Python.

Cette étape prépare le projet à être publié sur un index (comme PyPI) ou à être utilisé dans d'autres environnements de manière fiable. Le fichier généré est ensuite stocké comme artefact dans GitHub, ce qui permet de le récupérer facilement.

## Accès au package Python

Le package Python généré (.whl) est automatiquement archivé comme artefact dans votre workflow GitHub Actions. Pour y accéder :

1. Rendez-vous sur la page du dépôt GitHub : https://github.com/Al-vallon/ci_pokedex
2. Cliquez sur l'onglet "Actions"
3. Sélectionnez l'exécution du workflow concerné 
4. Dans la section "Artifacts" en bas de page, vous trouverez un élément nommé "superpokedex-package" (ou un nom similaire défini dans votre workflow)
5. Cliquez sur cet élément pour télécharger une archive zip contenant le fichier .whl

## Installation et utilisation du package

Une fois le package téléchargé, vous pouvez l'installer dans votre environnement Python :

```bash
# Installation directe du fichier wheel
pip install superpokedex-0.1.0-py3-none-any.whl

# Ou si vous avez décompressé l'archive
pip install chemin/vers/superpokedex-0.1.0-py3-none-any.whl
``` 

## Construction de l'image Docker

Une image Docker de l’application est construite à partir du Dockerfile présent à la racine du projet. Cette image contient tout ce qu’il faut pour exécuter l’application dans un conteneur, avec toutes ses dépendances.

Cette étape est essentielle pour garantir que l’environnement d’exécution est maîtrisé et cohérent entre développement, tests et production.

Publication de l’image Docker

Enfin, la dernière étape de la pipeline consiste à publier l’image Docker sur le registre GitHub Container Registry (ghcr.io). Une fois l’image construite, elle est taguée avec le nom du dépôt, puis poussée sur le registre. Cela permet à n’importe quel environnement distant (serveur de prod, plateforme d’hébergement, etc.) de tirer cette image directement depuis GitHub.

## Accès à l'image Docker

L'image Docker publiée est disponible à l'adresse suivante:
[https://github.com/Al-vallon/ci_pokedex/pkgs/container/superpokedex-web](https://github.com/Al-vallon/ci_pokedex/pkgs/container/superpokedex-web)

Vous pouvez récupérer l'image avec la commande:
```bash
docker pull ghcr.io/al-vallon/ci_pokedex/superpokedex-web:latest
```

La connexion au registre est effectuée de manière sécurisée via un token GitHub (GITHUB_TOKEN) pour s'assurer que seules les actions autorisées peuvent publier des images.

Résumé du flux d’exécution

Chaque fois qu’une modification est poussée sur main ou qu’une pull request est ouverte :

Le code est linté selon les règles définies dans setup.cfg.

Les tests du fichier test.py sont exécutés.

Une analyse statique de sécurité est réalisée avec CodeQL.

L’image Docker est construite et scannée avec Trivy.

Un package Python est généré.

L’image Docker est poussée vers le registre GitHub.

Cette pipeline apporte automatisation, sécurité, qualité et professionnalisme au processus de développement. Elle permet à toute l’équipe de travailler en confiance, avec des retours rapides à chaque modification.