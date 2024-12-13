from models.user import *

channelGL1 = Channel(101,"Genie Logiciel C4","GL")
channelGL2 = Channel(102,"Genie Civil et Mécanique","GLM")

teacher1 = Teacher(id=12,first_name="Manga",last_name="Joel",email='manga@gmail.com',user_name="manga",password="manga")
#anounce1 = teacher.create_anouncemnt(subjet="Emplois de temps Hebdomadaire",channel=channelGL1)
#anounce2 = teacher.create_anouncemnt(subjet="Programme pour les CC",channel=channelGL2)
#anounces = [anounce1, anounce2]
anounce1 = Anounce(
                  date_anounce=str(date.today()),
                  subjet="Programme pour les CC",
                  channel=channelGL1.to_json() ,
                  anounce_type="Media",
                  description="Remise des resultats Des étudiants de deuxieme année",
                  teacher=teacher1.to_json()
                  )
anounce2 = Anounce(
                  date_anounce=str(date.today()),
                  subjet="Emplois de temps Hebdomadaire",
                  channel=channelGL2.to_json(),
                  anounce_type="Media",
                  description="Emplois de temps Hebdomadaire",
                  teacher=teacher1.to_json()
                  )

anounces = [anounce1, anounce2]
 
student1 = Student(id="87669",first_name="Idris",last_name="Feudjio",email="idris@gmail.com",user_name="eva",password="baby",channel=channelGL1.to_json())

student2 = Student(id="87663",first_name="Idris",last_name="Feudjio",user_name="eva",email='eva@gmail.com'
                   ,password="baby",channel=channelGL2.to_json())

def init_sart():
    json_string = student1.to_json()
    dict_i = student1.from_json(json_string)
    s = student1.student_from_json(dict_i) 
    print(f'/////////////////////////////{dict_i}')
    print(f'/////////////////////////////{s.channel.class_name}')


def get_anounce_list() -> list[Anounce]:
    anounce_list = []
    anounce = anounces[0]
    json_string = anounce.to_json()
    dict_i = anounce.from_json(json_string)  
    an = anounce.annonce_from_json(dict_i)
    print(an.teacher.full_name())
    for anounce in anounces:
        json_string = anounce.to_json()
        dict_i = anounce.from_json(json_string)  
        an = anounce.annonce_from_json(dict_i)
        anounce_list.append(an)
    return anounce_list
 
#init_sart()
 