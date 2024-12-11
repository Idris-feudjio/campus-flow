from abc import ABC,abstractmethod
import json

class Serializer():
    def __init__(self) -> None:
        super().__init__()
    
    def to_json(self):
        return json.dumps(self.__dict__)
    
    def from_json(self,json_string):
        return json.loads(json_string)