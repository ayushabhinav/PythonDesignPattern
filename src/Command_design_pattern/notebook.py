""" These are the receiver function """

import sys


class Window:
    def exit(self):
        sys.exit()


class Document:
    def __init__(self, filename):
        self.filename = filename
        self.content = "This is a file"

    def save(self):
        with open(self.filename, "w") as outfile:
            outfile.write(self.content)


""" These are invoker code """


class ToolbarButton:
    def __init__(self, name, iconname) -> None:
        self.name = name
        self.icon = iconname

    def click(self):
        self.command.execute()


class MenuItems:
    def __init__(self, menu_name, menu_item_name) -> None:
        self.menu = menu_name
        self.menu_item_name = menu_item_name


class KeyboardShortcut:
    def __init__(self, key, modifier) -> None:
        self.key = key
        self.modifier = modifier

    def key_press(self):
        self.command.execute()


""" These are commaand code"""


class SaveCommand:
    def __init__(self, document):
        self.document = document

    def execute(self):
        self.document.save()


class ExitCommand:
    def __init__(self, window):
        self.window = window

    def execute(self):
        self.window.exit()


""" Binding Every thing together"""

window = Window()
document = Document("Ayush.txt")
save = SaveCommand(document)
exit = ExitCommand(window)

save_button = ToolbarButton("save", "save.png")
save_button.command = save

save_keystroke = KeyboardShortcut("s", "ctrl")
save_keystroke.command = save

exit_menu = MenuItems("File", "Exit")
exit_menu.command = exit
