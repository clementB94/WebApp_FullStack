
# WebApp_FullStack

Pour lancer 

1. ```docker-compose build``` (```docker-compose build --no-cache``` si besoin)
2. ```docker-compose up```

Utilisez soit le front-end (certains appels api ne sont pas encore disponibles) ou la documentation fast api pour avoir accès à toutes les requetes (nottament pour les utilisateurs).
  
## Front end : http://localhost:8080/
Réalisé avec Vue.js (https://vuejs.org/)
Communication avec l'API : axios



## Back-end : http://localhost:8000/docs
### API 
Réalisé avec FastAPI (https://fastapi.tiangolo.com/)

La documentation est accessible ici : http://localhost:8000/docs 

API : http://localhost:8000/

Une partie scraping est disponible au sein de l'API que l'on peut utiliser grace aux requetes :
- ``/movies/scrape/`` permettant de scraper un film avec son url IMDb
- ``/movies/most_rated/`` qui permet de scraper jusqu'à 250 films qui sont les mieux notés sur IMDb.

[Documentation scraping](http://localhost:8000/docs#/movies/scrape_top_movies_movies_most_rated_post)



### Base de donnée
Fonctionne avec PostgreSQL
  
Le dossier db_data a été enlevé du git. La database se charge en local à partir de rien à la création des conteneurs.
