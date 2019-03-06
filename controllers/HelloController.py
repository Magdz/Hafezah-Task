import json

from ..services import HelloService

class HelloController:
    def __init__(self):
        pass

    def hello_world(self):
        service = HelloService()
        values = service.hello_world()
        output = []
        for value in values:
            output.append({
                "id": value.id,
                "username": value.username,
                "email": value.email
            })
        return json.dumps(output)