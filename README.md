# Xavier Dupont de Pokédex

## Setup : 

> pip install -r requirements
>
>python manage.py migrate

Pour importer les données principales dans la base de données : 
>localhost:8000/internal/import/


## Fonctionnalités back-end : 

- Joueur : 
    - Ajout d'un joueur
    - Authentification
- Pokémon : 
    - Ajout d'un pokémon aléatoire (pour des tests) ou donné (pour une capture)
    - Création d'une équipe de pokémons
    - Ajout d'un pokémon à une équipe
    - Rencontre d'un pokémon dans une Zone donnée
- Inventaire :
    - Ajout d'un objet (pokéball ou potion)
    
    
## Problèmes actuels : 

- Front : 
    - Pas de lien entre les templates et les datas
   
- Back  :
    - Pas d'utilisation des items
    - Mauvaise gestion des moves lors de l'import
    
    
## Contributeurs : 

- Benjamin STRABACH
- Alexandre GAULTIER
- Anaïs TATIBOUET
- Maxime MONNIER
- Sylouan CORFA