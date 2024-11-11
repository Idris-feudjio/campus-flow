from models.user import *

student_list = [
   Student(first_name="Idris",last_name="Feudjio",user_name="eva",password="baby",channel=channelGL1),
   Student(first_name="TALA",last_name="ANDRE",user_name="mari",password="mari",channel=channelGL2)
]

channel_list = [
    Channel(101,"Genie Logiciel"),
    Channel(102,"RSA")
]






channelGL1 = Channel(101,"Genie Logiciel C4")
channelGL2 = Channel(102,"Genie Logiciel B2")

teacher = Teacher(first_name="Manga",last_name="Joel",user_name="manga",password="manga")
anounce1 = teacher.create_anouncemnt(subjet="Emplois de temps Hebdomadaire",channel=channelGL1)
anounce2 = teacher.create_anouncemnt(subjet="Programme pour les CC",channel=channelGL2)
anounces = [anounce1, anounce2]

student1 = Student(first_name="Idris",last_name="Feudjio",user_name="eva",password="baby",channel=channelGL1)

student2 = Student(first_name="Idris",last_name="Feudjio",user_name="eva",password="baby",channel=channelGL2)

anounces_student = student1.get_anouncement(anounces_list=anounces) 