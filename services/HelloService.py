from ..repositories import OwnerRepository

class HelloService:
    def __init__(self):
        pass

    def hello_world(self):
        repository = OwnerRepository()
        return repository.all()