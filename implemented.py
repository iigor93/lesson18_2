from setup_db import db
from dao.models_dao.movies_dao import MoviesDAO
from service.movie_service import MovieService
from dao.models_dao.directors_dao import DirectorDAO
from service.director_service import DirectorService
from dao.models_dao.genres_dao import GenreDAO
from service.genre_service import GenreService


movie_dao_object = MoviesDAO(db.session)
movie_service_obj = MovieService(movie_dao_object)


director_dao_object = DirectorDAO(db.session)
director_service_obj = DirectorService(director_dao_object)


genre_dao_object = GenreDAO(db.session)
genre_service_obj = GenreService(genre_dao_object)
