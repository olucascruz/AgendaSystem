from repositories.event_repository import EventRepository
from usecases.event_usecase import EventUsecase
from controllers.event_controller import EventController

def event_factory():
    event_repository = EventRepository()
    event_usecase = EventUsecase(event_repository)
    event_controller = EventController(event_usecase)

    return event_controller
