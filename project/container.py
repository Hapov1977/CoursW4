from project.dao import GenresDAO, MoviesDAO, UsersDAO, DirectorsDAO

from project.services import GenresService, DirectorsService, MoviesService, UsersService
from project.setup.db import db

# DAO
genre_dao = GenresDAO(db.session)
director_dao = DirectorsDAO(db.session)
movie_dao = MoviesDAO(db.session)
user_dao = UsersDAO(db.session)

# Services
genre_service = GenresService(dao=genre_dao)
director_service = DirectorsService(dao=genre_dao)
movie_service = MoviesService(dao=genre_dao)
user_service = UsersService(dao=genre_dao)
