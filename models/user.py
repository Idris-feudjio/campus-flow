from datetime import date 
from share.functions.base_fire_b_crud import *
from share.functions.abstract_serializer import *


class Channel (Serializer): 
     def __init__(self,class_code,class_name,short_name) -> None:
        self.class_code = class_code
        self.class_name = class_name
        self.short_name = short_name
        super().__init__()
        
     def channel_from_json(json_s):
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
    
    def full_name(self):
        return f'{self.first_name } {self.last_name}'
    
    
class Student (User):
    def __init__(self, first_name, last_name, email, user_name, password, channel: Channel = None, id=None, avatar=None):
        super().__init__(first_name, last_name, email, user_name, password, channel, id, avatar)
    
    @staticmethod
    def student_from_json(json_s):
        c = Channel("","","").from_json(json_s["channel"])
        chan = Channel.channel_from_json(c)
        return Student(id=json_s["id"],
                       first_name=json_s["first_name"],
                       last_name=json_s["last_name"],
                       user_name=json_s["user_name"],
                       email=json_s["email"],
                       avatar=json_s["avatar"],
                       password=json_s["password"],
                       channel=chan,
                       )
          
class Teacher(User):
    def __init__(self, first_name, last_name, email, user_name, password, id=None, avatar=None):
        super().__init__(first_name, last_name, email, user_name, password, id, avatar)
    
    @staticmethod
    def teacher_from_json(json_s):  
        return Teacher(id=json_s["id"],
                    first_name=json_s["first_name"],
                    last_name=json_s["last_name"],
                    user_name=json_s["user_name"],
                    email=json_s["email"],
                    avatar=json_s["avatar"],
                    password=json_s["password"], 
                    )  

class Anounce(Serializer): 
    def __init__(self,date_anounce,subjet,channel:Channel,anounce_type,description,teacher:Teacher ) -> None:
        self.date_anounce = date_anounce
        self.subjet = subjet
        self.channel = channel
        self.anounce_type = anounce_type # Text, Multimedia
        self.description = description
        self.teacher = teacher
        super().__init__()
        
    @staticmethod
    def annonce_from_json(json_s): 
        
        c = Channel("","","").from_json(json_s["channel"])
        chan = Channel.channel_from_json(c) 
        
        t = Teacher("","","","","","").from_json(json_s["teacher"]) 
        teacher = Teacher.teacher_from_json(t) 
        return Anounce(date_anounce=json_s["date_anounce"],
                       subjet=json_s["subjet"],
                       channel=chan,
                       anounce_type=json_s["anounce_type"],
                       description=json_s["description"],
                       teacher= teacher,
                       )
    