class Menu:
    def __init__ (self, title, prompt):
        """
        Menu (title:str, prompt:str)
        Creates a new menu with title and prompt
        """
        self.title = title
        self.prompt = prompt
        self.options = []
        self.options.append([0,"Salir"])

    def add (self, name:str):
        """
        add (name:str)
        Adds the option name to the menu
        """
        self.options.append([name, len(self.options)])

    def add (self, name:str, number:int):
        """
        add (name:str, number:int)
        Adds the option name to the menu with the number.
        """
        self.options.append([name, number])

    def addAll (self, names):
        """
        add (name:str[])
        Adds all the options to the menu
        """
        for option in names:
            self.add(option)

    def runSelection (self):
        """
        runSelection (void)
        Runs the selection for this menu.
        Returns the number the user selects.
        """
        print(self.title)
        for i in range (len(self.options)):
            print(self.options[i][1], ". ", self.options[i][0], sep="")
        print(self.prompt, end="")
        return int(input())