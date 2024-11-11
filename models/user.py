from datetime import date
import json 

class Channel:
    def __init__(self,num_class,class_name) -> None:
        self.num_class = num_class
        self.class_name = class_name

class User:
    number_of_user  = 0
    def __init__(self,first_name,last_name,user_name,password,channel = None) :
        self.first_name = first_name
        self.last_name =last_name
        self.password= password
        self.user_name = user_name
        self.channel = channel

    #def print_info(self) -> str:
     #  return f"Nom : {self.last_name}, Prenom : {self.first_name},  Nom utilisateur : {self.user_name}, Password #: ***** "
    

class Student (User):
    annonce_number = 0
    def __init__(self, first_name, last_name, user_name, password, channel):
        super().__init__(first_name, last_name, user_name, password, channel)
    
    def get_anouncement(self,anounces_list):
        return [anounce for anounce in anounces_list if anounce.channel==self.channel]
    
class Teacher(User):
    def __init__(self, first_name, last_name, user_name, password, channel=None):
        super().__init__(first_name, last_name, user_name, password, channel)   

    def create_anouncemnt(self,subjet,channel):
        return Anounce(date.today(),subjet,channel)

class Anounce:
    def __init__(self,date_anounce,subjet,channel) -> None:
        self.date_anounce = date_anounce
        self.subjet = subjet
        self.channel = channel

channelGL1 = Channel(101,"Genie Logiciel C4")
channelGL2 = Channel(102,"Genie Logiciel B2")

teacher = Teacher(first_name="Manga",last_name="Joel",user_name="manga",password="manga")
anounce1 = teacher.create_anouncemnt(subjet="Emplois de temps Hebdomadaire",channel=channelGL1)
anounce2 = teacher.create_anouncemnt(subjet="Programme pour les CC",channel=channelGL2)
anounces = [anounce1, anounce2]

student1 = Student(first_name="Idris",last_name="Feudjio",user_name="eva",password="baby",channel=channelGL1)

student2 = Student(first_name="Idris",last_name="Feudjio",user_name="eva",password="baby",channel=channelGL2)

anounces_student = student1.get_anouncement(anounces_list=anounces) 
print(student1.__dict__)

for anounce in anounces_student:
    print(f"Filière: {anounce.channel.class_name}, Annonce: {anounce.subjet}, Date : {anounce.date_anounce}")