# Simple enough, just import everything from tkinter.
from tkinter import *



# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        
        # parameters that you want to send through the Frame class. 
        Frame.__init__(self, master)   

        #reference to the master widget, which is the tk window                 
        self.master = master

        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("GUI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        quitButton = Button(self, text="Exit", command=self.client_exit)
        quitButton.place(x=370, y=0)
        clickButton = Button(self, text="Click_me", command=self.clicker)
        clickButton.place(x=160, y=0)
        twitchButton = Button(self, text="links", command=self.twitch)
        twitchButton.place(x=0, y=374)


        # create the file object)
        file = Menu(menu)
        edit=Menu(menu)
        
        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        file.add_command(label="Exit", command=self.client_exit)
        file.add_command(label="Click_Me", command=self.clicker)
        file.add_command(label="links", command=self.twitch)

        #added "file" to our menu
        menu.add_cascade(label="File", menu=file)

        # create the file object)
        edit = Menu(menu)


        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        edit.add_command(label="Undo")

        #added "file" to our menu
        menu.add_cascade(label="Edit", menu=edit)


        medit = Menu(menu)
        medit.add_command(label="Dum Dum")
        menu.add_cascade(label="Nothing here (do not click)", menu=medit)

    def twitch(self):
        print ("you should folow my twitch ------> (www.twitch.tv/lleryt)")
        print ("while your there follow (www.twitch.tv/Nedya121)")
    def clicker(self):
        print ("yay it worked")
    def client_exit(self):
        exit()

        
# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

root.geometry("400x400")

#creation of an instance
app = Window(root)

#mainloop 
root.mainloop()  
