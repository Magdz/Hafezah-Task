from ..services import HelloService

class HelloController:
    def __init__(self, app):
        self.app = app

    def hello_world(self):
        service = HelloService(self.app)
        return service.hello_world()