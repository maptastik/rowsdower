import PySimpleGUI as sg
from rowsdower import rowsdower

layout = [
    [
        sg.Text('Authentication', text_color = "#A9C13F", background_color = "#003242", font = 'Arial 16')
    ], [
        sg.Text('Portal URL', size = (10, 1), text_color = "#ECECEC", background_color = "#003242"), sg.InputText(key = "portal", size = (32, 1))
    ], [
        sg.Text('Username', size = (10, 1), text_color = "#ECECEC", background_color = "#003242"), sg.InputText(key = "username", size = (32, 1))
    ], [
        sg.Text('Password', size = (10, 1), text_color = "#ECECEC", background_color = "#003242"), sg.InputText(key = "password", password_char = "*", size = (32, 1))
    ], [
        sg.Text('Table Info', text_color = "#A9C13F", background_color = "#003242", font = 'Arial 16')
    ], [
        sg.Text('Item ID', size = (10, 1), text_color = "#ECECEC", background_color = "#003242"), sg.InputText(key = "item", size = (32, 1)) 
    ], [
        sg.Text('Table Name', size = (10, 1), text_color = "#ECECEC", background_color = "#003242"), sg.InputText(key = "table", size = (32, 1))
    ], [
        sg.Text('Temporary Value Field', size = (16, 1), text_color = "#ECECEC", background_color = "#003242"), sg.InputText(key = "field", size = (22, 1))
    ], [
        sg.Text('# Rows to add (max. 5)', size = (20, 1), text_color = "#ECECEC", background_color = "#003242"), sg.Slider(key = "count", range = (1, 5), resolution = 1, orientation = 'h', size = (14, 15), default_value = 1, text_color = "#ECECEC", background_color = "#003242")
    ], [
        sg.Button('Run', tooltip = 'Click to add rows to table', bind_return_key = True, button_color = ("#ECECEC", "#4C8C2B"), auto_size_button = True, font = 'Arial 16')
    ]
]

window = sg.Window('rowsdower', layout, background_color = "#003242")

while True:
    event, values = window.Read()
    if event == "Run":
        try:
            rowsdower(
                values["portal"],
                values["username"],
                values["password"],
                values["item"],
                values["table"],
                values["field"],
                int(values["count"])
            )
        except Exception as e:
            print(e)
        finally:
            window.Close()
    else:
        break