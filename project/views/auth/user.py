from flask import request
from flask_restx import Namespace, Resource

from project.container import user_service
from project.setup.api.models import user

api = Namespace('user')


@api.route('/')
class RegisterView(Resource):
    @api.marshal_with(user, as_list=True, code=200, description='OK')
    def patch(self):
        data = request.json
        header = request.headers.get('HTTP_AUTHORIZATION').replace('Bearer','')

        return user_service.update_user(data=data, refresh_token=header)

    @api.marshal_with(user, as_list=True, code=200, description='OK')
    def get(self):
        header = request.headers.get('HTTP_AUTHORIZATION').replace('Bearer','')

        return user_service.get_user_by_token(refresh_token=header)


@api.route('/password/')
class LoginView(Resource):
    def put(self):
        data = request.json
        header = request.headers.get('HTTP_AUTHORIZATION').replace('Bearer','')

        return user_service.update_password(data=data, refresh_token=header)


@api.doc(security='Bearer')
@api.response(code=401, description='Authorization needed', model=error)
@api.response(code=404, description='Bad request', model=error)
@api.route('/', endpoint='profile_view')
class UserProfileView(Resource):

    @api.marshal_with(user_profile, code=200, description='OK')
    @login_required
    def get(self, user_id: int):
        """
        Получить профиль пользователя.
        """
        return UsersService(db.session).get_user_profile(user_id)