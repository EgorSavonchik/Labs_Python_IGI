import container

class containerCLI :

    def start(self) :
        self.storage = container.Container(input("Enter username "))
        self.storage.load()

        print("select actions: \n1) add \n2) remove \n3) find \n4) list \n5) grep \n6) save \n7) load \n8) switch \n9) exit")

        command = input()

        while(command != "exit") :
            match(command.split(" ")[0]) :
                case "add" :
                    self.storage.add(command[4::].split(", "))
                case "remove" :
                    self.storage.remove(command.split(" ")[1])
                case "find" :
                    self.storage.find(command[5::].split(", "))
                case "list" :
                    self.storage.list()
                case "grep" :
                    self.storage.grep(command.split(" ")[1])
                case "save" :
                    self.storage.save()
                case "load" :
                    self.storage.load()
                case "switch" :
                    match(input("you want save container?").lower()) :
                        case "yes" :
                            self.storage.save()
                        case "no" :
                            pass
                        case _ : 
                            print("try again")

                    self.storage.switch(command.split(" ")[1])

                    match(input("You want dowload container?").lower()) :
                        case "yes" :
                            self.storage.load()
                        case "no" :
                            pass
                        case _ :
                            print("try again")
                case _ :
                    print("Command not found")

            command = input()
            




    