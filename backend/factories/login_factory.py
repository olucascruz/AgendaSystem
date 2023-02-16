from repositories.user_repository import UserRepository
from usecases.login_usecase import LoginUsecase
from controllers.login_controller import LoginController

def login_factory():
    user_repository = UserRepository()
    login_usecase = LoginUsecase(user_repository)
    login_controller = LoginController(login_usecase)

    return login_controller
    