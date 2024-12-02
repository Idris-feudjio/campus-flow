from datetime import date 
from share.functions.base_fire_b_crud import *
from share.functions.abstract_serializer import *


class Channel (Serializer): 
     def __init__(self,class_code,class_name,short_name) -> None:
        self.class_code = class_code
        self.class_name = class_name
        self.short_name = short_name
        super().__init__()
        
     def channel_from_json(self,json_s):
        return Channel(class_code=json_s["class_code"],
                       class_name=json_s["class_name"],
                       short_name=json_s["short_name"], 
                       )
   
class User(Serializer) :
    def __init__(self,first_name,last_name,email,user_name,password,channel :Channel= None,id=None,avatar=None) :
        self.id =id
        self.first_name = first_name
        self.last_name =last_name
        self.user_name = user_name
        self.channel = channel
        self.email = email
        self.avatar = avatar
        self.password= password
        super().__init__()
    
    
class Student (User):
    def __init__(self, first_name, last_name, email, user_name, password, channel: Channel = None, id=None, avatar=None):
        super().__init__(first_name, last_name, email, user_name, password, channel, id, avatar)
        
    def student_from_json(self,json_s):
        return Student(id=json_s["id"],
                       first_name=json_s["first_name"],
                       last_name=json_s["last_name"],
                       user_name=json_s["user_name"],
                       email=json_s["email"],
                       avatar=json_s["avatar"],
                       password=json_s["password"],
                       channel=json_s["channel"],
                       )
          
class Teacher(User):
    def __init__(self, first_name, last_name, email, user_name, password, channel: Channel = None, id=None, avatar=None):
        super().__init__(first_name, last_name, email, user_name, password, channel, id, avatar)
        
        def teacher_from_json(self,json_s):
            return Teacher(id=json_s["id"],
                       first_name=json_s["first_name"],
                       last_name=json_s["last_name"],
                       user_name=json_s["user_name"],
                       email=json_s["email"],
                       avatar=json_s["avatar"],
                       password=json_s["password"],
                       channel=json_s["channel"],
                       )

class Anounce(Serializer): 
    def __init__(self,date_anounce,subjet,channel:Channel,anounce_type,description,teacher:Teacher ) -> None:
        self.date_anounce = date_anounce
        self.subjet = subjet
        self.channel = channel
        self.type = anounce_type # Text, Multimedia
        self.description = description
        self.teacher = teacher
        super().__init__()
    
    def annonce_from_json(self,json_s):
        return Anounce(date_anounce=json_s["date_anounce"],
                       subjet=json_s["subjet"],
                       channel=json_s["channel"],
                       type=json_s["type"],
                       description=json_s["description"],
                       teacher=json_s["teacher"],
                       )
    