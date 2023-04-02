# img_viewer.py

import PySimpleGUI as sg
import os.path

# ----- Full layout -----
layout = [
    [
        [
            sg.Text('So ky tu trong moi phep tinh'),
            sg.InputText()
        ],
        [
            sg.Text('So phep tinh'),
            sg.InputText()
        ],
        [
            sg.Text('Thoi gian hien thi'),
            sg.InputText()
        ]

    ],
    [
        sg.HorizontalSeparator(),

        sg.Text("Play"),
    ]
]

window = sg.Window("Quick Math", layout)

# Run the Event Loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    # Folder name was filled in, make a list of files in the folder
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            # Get list of files in folder
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
               and f.lower().endswith((".png", ".gif"))
        ]
        window["-FILE LIST-"].update(fnames)
    elif event == "-FILE LIST-":  # A file was chosen from the listbox
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )
            window["-TOUT-"].update(filename)
            window["-IMAGE-"].update(filename=filename)

        except:
            pass

window.close()
