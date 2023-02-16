from repositories.user_repository import UserRepository
from usecases.user_usecase import UserUsecase
from controllers.user_controller import UserController

def user_factory():
    user_repository = UserRepository()
    user_usecase = UserUsecase(user_repository)
    user_controller = UserController(user_usecase)

    return user_controller
    