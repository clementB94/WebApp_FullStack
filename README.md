

# WebMovie FullStack

Application d'avis sur des films permettant de communiquer avec une API via une interface Vue.js. Cet API permet de scraper des films directement sur [IMDb](https://www.imdb.com/) et de les enregistrer dans une base de donnée. Les utilisateurs peuvent ensuite noter les films ou ajouter des commentaires. 




## Pour lancer 

Pour faciliter l'installation il est possible d'utiliser une base par défaut avec des utilisateurs et des commentaires déjà présents (cf. "Base de donnée").

1. ```docker-compose build``` (```docker-compose build --no-cache``` si besoin)
2. ```docker-compose up```

Utilisez soit le front-end (certains appels api ne sont pas encore disponibles) ou la documentation fast api pour avoir accès à toutes les requetes (nottament pour les utilisateurs). 
  
## Front end : http://localhost:8080/
Réalisé avec Vue.js (https://vuejs.org/)

Communication avec l'API : axios

Pages disponibles : 
- Accueil
- Liste de films sur la base
- Informations sur un film (avec évalution et commentaires)
- Scraping d'un film à partir d'un lien IMDb
- Profil utilisateur (avec ses évaluations et commentaires)

Le front-end ne fonctionne pour le moment qu'avec l'utilisateur **admin**. En effet, l'authentification d'un utilisateur ne peut peut pas encore se faire à partir du front-end mais est disponible via l'API : [Tester via la requete ``/users/token/test``](http://localhost:8000/docs#/default/test_user_auth_users_token_test_get) après que vous vous soyez identifié avec un utilisateur existant dans la base. (Authorize sur la documentation fast api). Cependant, les autres api sont utilisables sans authentification.

**Le mot de passe de l'utilisateur "admin" est "azerty".**

## Back-end : http://localhost:8000/docs
### API 
Réalisé avec FastAPI (https://fastapi.tiangolo.com/) et SQLAlchemy (https://www.sqlalchemy.org/).

La documentation est accessible ici : http://localhost:8000/docs 

API : http://localhost:8000/

Une partie scraping est disponible au sein de l'API que l'on peut utiliser grace aux requetes :
- ``/movies/scrape/`` permettant de scraper un film avec son url IMDb. ex : https://www.imdb.com/title/tt0068646/
- ``/movies/most_rated/`` qui permet de scraper automatiquement jusqu'à 250 films qui sont les mieux notés sur IMDb.

[Documentation scraping](http://localhost:8000/docs#/movies/scrape_top_movies_movies_most_rated_post)



### Base de donnée
Fonctionne avec PostgreSQL
  
Une base de donnée par défaut a été ajouté au git dans db_data.zip qu'il suffit d'extraire. Il est tout à fait possible de supprimer le dossier db_data ainsi créé afin d'en recréer une vide automatiquement à la construction des conteneurs Docker. **Cela necessite de recréer un utilisateur "admin" à la main avant de pouvoir utiliser le front-end.**

-----

Bonne découverte !
