from flet import *
from share.db.auth import *

def DashboardView(page:Page, myPyrebase:PyrebaseWrapper):
    title = "My Dashboard"

    username = Text("Welcome", size=16)

    def handle_stream(message):
        try:
            build_notes()
            page.update()
        except:
            pass

    def on_page_load():
        clean_notes()
        username.value = "Welcome"
        if myPyrebase.check_token() == "Success":
            myPyrebase.stream_data(handle_stream)
            handle = myPyrebase.get_username()
            if handle:
                username.value = "Welcome, " + "@" + handle
            page.update()
     

    def handle_add(e):
        myPyrebase.add_note({"note": note_field.value})
        note_field.value = ""
        page.update()
        
    def handle_logout(*e):
        clean_notes()
        username.value = ""
        myPyrebase.kill_all_streams()
        myPyrebase.sign_out()
        page.go("/")

    
    note_field = TextField(label="Enter note here", width=250)
    all_notes = []

    def build_notes():
        all_notes.clear()
        data = myPyrebase.get_notes()
        keys = data['notes'].keys()
        for key in keys:
            note_text = data['notes'][key]['note']
           # note = Note(page, note_text, key, myPyrebase)
            #all_notes.append(note)

    def clean_notes():
        all_notes.clear()
        all_notes.append(Text(" "))
        page.update()


    add_note_button = TextButton("Add Note", on_click=handle_add)
    logout_button = TextButton("Logout", on_click=handle_logout, style=ButtonStyle(colors.RED))


    myPage = Column([
            Row([Text("Dashboard", size=20)], alignment=MainAxisAlignment.CENTER),
            Row([username], alignment=MainAxisAlignment.CENTER),
            Column(all_notes, alignment="center"),
            Row([note_field], alignment=MainAxisAlignment.CENTER),
            Row([add_note_button], alignment=MainAxisAlignment.CENTER),
            Row([logout_button], alignment=MainAxisAlignment.CENTER)
            ])
            
    return {
        "view":myPage,
        "title": title,
        "load": on_page_load
        }