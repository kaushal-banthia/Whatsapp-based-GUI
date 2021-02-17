# Importing the relevant modules
from os import path
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
from tkinter.font import Font
import matplotlib.pyplot as plt
from PIL import ImageTk
from PIL import Image

# Kaushal Banthia
# 19CS10039

# Class for selecting the current user
class Select_User:

    # Constructor
    def __init__(self):
        self.root = Toplevel(root)
        self.label = Label(self.root, text = "Select the User :",  font = ("Times New Roman", 10))
        self.user_chosen = Combobox(self.root, values = [i for i in users_obj.keys()], state = "readonly")
        
    # Function to pack the widgets
    def pack(self):
        self.label.grid(column = 0,  row = 0, padx = 10, pady = 25)
        self.user_chosen.grid(column = 1, row = 0)
        self.user_chosen.current(0)

# Class to display the contacts of the selected user (selected using the Select_User Base Class)
class Display_Contacts(Select_User):

    # Constructor
    def __init__(self):
        super().__init__()
        super().pack()
        self.root.title("Contacts of the Chosen User")
        self.contacts_label = []

        self.chosen_users_id = None
        Button(self.root, text = "Select", command = self.select).grid(column = 0, rows = 1, columnspan = 2)
        self.c_label = None

        # Packing all the widgets
        self.pack()
    
    # Function called on pressing the button
    def select(self):
        for i in range(len(self.contacts_label)):
            self.contacts_label[i].config(text = '')
        self.pack()

        self.contacts_label = []
        self.chosen_users_id = self.user_chosen.get()
        if (self.chosen_users_id != None):
            for i in users_obj[self.chosen_users_id].contacts:
                self.contacts_label.append(Label(self.root, text = i))
        
        self.c_label = Label(self.root, text = "The contacts of " + str(self.chosen_users_id) + " are:")
        self.pack()

    # Function to pack the widgets
    def pack(self):
        if self.c_label != None:
            self.c_label.grid(row = 2, column = 0)
        counter = 2
        for i in self.contacts_label:
            i.grid(row = counter, column = 1, columnspan = 2)
            counter+=1

# Class to display the groups of the selected user (selected using the Select_User Base Class)
class Display_Groups(Select_User):

    # Constructor
    def __init__(self):
        super().__init__()
        super().pack()

        self.root.title("Groups of the chosen User")
        self.groups_label = []

        self.chosen_users_id = None
        Button(self.root, text = "Select", command = self.select).grid(column = 0, rows = 1, columnspan = 2)
        self.g_label = None

        # Packing all the widgets
        self.pack()

    # Function called on pressing the button
    def select(self):
        for i in range(len(self.groups_label)):
            self.groups_label[i].config(text = '')
        self.pack()

        self.groups_label = []
        self.chosen_users_id = self.user_chosen.get()
        if (self.chosen_users_id != None):
            for i in users_obj[self.chosen_users_id].in_these_groups:
                self.groups_label.append(Label(self.root, text = i.group_id))
        
        self.g_label = Label(self.root, text = "The groups of " + str(self.chosen_users_id) + " are:")
        self.pack()

    # Function to pack the widgets
    def pack(self):
        if self.g_label != None:
            self.g_label.grid(row = 2, column = 0)
        counter = 2
        for i in self.groups_label:
            i.grid(row = counter, column = 1, columnspan = 2)
            counter+=1

# Class to display the received messages of the selected user (selected using the Select_User Base Class)
class Display_Messages(Select_User):

    # Constructor
    def __init__(self):
        super().__init__()
        super().pack()
        self.root.title("Messages received by the User")
        self.messages_label = []

        self.chosen_users_id = None
        Button(self.root, text = "Select", command = self.select).grid(column = 0, rows = 1, columnspan = 2)
        self.m_label = Label(self.root, text = "")

        # Packing all the widgets
        self.pack()

    # Function called on pressing the button
    def select(self):
        for i in range(len(self.messages_label)):
            if self.messages_label[i]['image'] == None or self.messages_label[i]['image'] == '':
                self.messages_label[i].config(text = '')
            else:
                self.messages_label[i].config(image = '')
        self.pack()

        self.messages_label = []
        self.chosen_users_id = self.user_chosen.get()
        if (self.chosen_users_id != None):
            for i in users_obj[self.chosen_users_id].received_messages:
                if 'C:/' in str(i):
                    image = str(i).split(" [")[0]
                    self.messages_label.append(image)
                    self.messages_label.append(Label(self.root, text = '[' + str(i).split(" [")[1]))
                else:
                    self.messages_label.append(Label(self.root, text = i))
        
        self.m_label.config(text = "The messages received by " + str(self.chosen_users_id) + " are:")
        self.pack()
    
    # Function to pack the widgets
    def pack(self):
        if self.m_label != None:
            self.m_label.grid(row = 2, column = 0)
        counter = 2
        x = 0
        while x < len(self.messages_label):
            if 'C:/' in str(self.messages_label[x]):
                img = Image.open(self.messages_label[x][2:])
                img = img.resize((250, 250), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(img)
                panel = Label(self.root, image = img)
                panel.image = img
                self.messages_label[x] = panel
                panel.grid(row = counter, column = 1)
                counter += 1
                x += 1
                self.messages_label[x].grid(row = counter, column = 1, columnspan = 2)

            else:
                self.messages_label[x].grid(row = counter, column = 1, columnspan = 2)
            counter+=1
            x+=1

# Class to send messages from the selected user (selected using the Select_User Base Class)
class Send_Messages(Select_User):

    # Constructor
    def __init__(self):
        super().__init__()
        super().pack()
        self.root.title("Send message")
        self.filname = None
        self.l1 = []
        self.l2 = []

        # Declaration of all the widgets at one place
        self.ru_label = Label(self.root, text = "Select the receiver user")
        self.user_to_whom_message_is_to_sent = Combobox(self.root, values = self.l1, state = "readonly")
        self.rg_label = Label(self.root, text = "Select the receiver group")
        self.group_to_which_message_is_to_be_sent = Combobox(self.root, values = self.l2, state = "readonly")
        self.it_label = Label(self.root, text = "Do you want to send an image or a text message")
        self.image_or_text = Combobox(self.root, values = ["Image", "Text"], state = "readonly")
        self.button_choose = Button(self.root, text = "Select", command = self.choose)
        self.mt_label = Label(self.root, text = '')
        self.messagebox = Text(self.root, height = 5, width = 30)
        self.sender_button = Button(self.root, text = "Send", command = self.send)
        self.image_selector_button = Button(self.root, text = "Select Image", command = self.openfilename)
        self.chosen_users_id = None
        Button(self.root, text = "Select Sender", command = self.select).grid(column = 0, rows = 1, columnspan = 2)

        # Packing all the widgets
        self.pack()

    # Function called on pressing the button
    def select(self):
        self.chosen_users_id = self.user_chosen.get()
        self.l1 = [i for i in users_obj[self.chosen_users_id].contacts]
        self.l1.insert(0, "Choose")
        self.user_to_whom_message_is_to_sent.config(values = self.l1)
    
        self.l2 = [i.group_id for i in users_obj[self.chosen_users_id].in_these_groups]
        self.l2.insert(0, "Choose")
        self.group_to_which_message_is_to_be_sent.config(values = self.l2)
        self.pack(from_select = 1)

    # Function called on pressing the button 'button_choose'
    def choose(self):
        if self.image_or_text.get() == "Image":

            # add an image
            self.messagebox.destroy()
            self.sender_button.destroy()

            if not self.image_selector_button.winfo_exists():
                self.image_selector_button = Button(self.root, text = "Select Image", command = self.openfilename)
            if not self.sender_button.winfo_exists():
                self.sender_button = Button(self.root, text = "Send", command = lambda: self.send(1))

            if str(self.group_to_which_message_is_to_be_sent.get()) == 'Choose' and str(self.user_to_whom_message_is_to_sent.get()) == 'Choose':
                self.mt_label.config(text = "Please Select at least one person or group")
                self.image_selector_button.config(state = DISABLED)
                self.sender_button.config(state = DISABLED)
            else:
                self.mt_label.config(text = "Select the Image: ")
                self.image_selector_button.config(state = NORMAL)
                self.sender_button.config(state = NORMAL)
            self.pack(from_choose = 1, is_this_for_image = 1)
            
        elif self.image_or_text.get() == "Text":
            
            # add text
            self.image_selector_button.destroy()
            self.sender_button.destroy()

            if not self.messagebox.winfo_exists():
                self.messagebox = Text(self.root, height = 5, width = 30)
            if not self.sender_button.winfo_exists():
                self.sender_button = Button(self.root, text = "Send", command = self.send)

            if str(self.group_to_which_message_is_to_be_sent.get()) == 'Choose' and str(self.user_to_whom_message_is_to_sent.get()) == 'Choose':
                self.mt_label.config(text = "Please Select at least one person or group")
                self.messagebox.config(state = DISABLED)
                self.sender_button.config(state = DISABLED)
            else:
                self.mt_label.config(text = "Enter your message: ")
                self.messagebox.config(state = NORMAL)
                self.sender_button.config(state = NORMAL)
            self.pack(from_choose = 1)

    # Function called on pressing the button 'image_selector_button'
    def openfilename(self):
        self.filename = filedialog.askopenfilename(title ='Choose Image') 

    # Function called on pressing the button 'sender_button'
    def send(self, send_image = 0):
        if send_image == 1:
            if str(self.filename) == '':
                new_root = Toplevel(root)
                Label(new_root, text = "Cannot Send Empty Image").pack()
                Button(new_root, text = "Close", command = lambda: exit(new_root)).pack()
                return
            
            # opening the file in append mode also ensures that if the file is not present then it will create it
            f = open("messages.txt", "a")

            if str(self.user_to_whom_message_is_to_sent.get()) != "Choose":
                user_id_of_receiver = self.user_to_whom_message_is_to_sent.get()
                text_to_be_sent = "->" + str(self.filename) + " [Sender: " + str(self.chosen_users_id) + "]"
                
                users_obj[user_id_of_receiver].received_messages.append(text_to_be_sent)
                f.write(text_to_be_sent + '\n')
                f.write(user_id_of_receiver + '\n')
            if (self.group_to_which_message_is_to_be_sent.get()) != "Choose":
                group_id_of_receiver = self.group_to_which_message_is_to_be_sent.get()
                for i in groups_obj[group_id_of_receiver].members:
                    if i.user_id != self.chosen_users_id:
                        # send to the users of the groups that are not the sender itself
                        text_to_be_sent = "->" + self.filename + " [Sender: " + str(self.chosen_users_id) + ", Group: " + str(group_id_of_receiver) + "]"
                        
                        i.received_messages.append(text_to_be_sent)
                        f.write(text_to_be_sent + '\n')
                        f.write(i.user_id + '\n')
            
        else:
            if self.messagebox != None:
                if str(self.messagebox.get("1.0",'end-1c')) == '':
                    new_root = Toplevel(root)
                    Label(new_root, text = "Cannot Send Empty Message").pack()
                    Button(new_root, text = "Close", command = lambda: exit(new_root)).pack()
                    return
                
                # opening the file in append mode also ensures that if the file is not present then it will create it
                f = open("messages.txt", "a")

                if str(self.user_to_whom_message_is_to_sent.get()) != "Choose":
                    user_id_of_receiver = self.user_to_whom_message_is_to_sent.get()
                    text_to_be_sent = "->" + self.messagebox.get("1.0",'end-1c') + " [Sender: " + str(self.chosen_users_id) + "]"
                    
                    users_obj[user_id_of_receiver].received_messages.append(text_to_be_sent)
                    f.write(text_to_be_sent + '\n')
                    f.write(user_id_of_receiver + '\n')
                if (self.group_to_which_message_is_to_be_sent.get()) != "Choose":
                    group_id_of_receiver = self.group_to_which_message_is_to_be_sent.get()
                    for i in groups_obj[group_id_of_receiver].members:
                        if i.user_id != self.chosen_users_id:
                            # send to the users of the groups that are not the sender itself
                            text_to_be_sent = "->" + self.messagebox.get("1.0",'end-1c') + " [Sender: " + str(self.chosen_users_id) + ", Group: " + str(group_id_of_receiver) + "]"
                            
                            i.received_messages.append(text_to_be_sent)
                            f.write(text_to_be_sent + '\n')
                            f.write(i.user_id + '\n')

                self.messagebox.delete("1.0", "end")

    # Function to pack all the widgets
    def pack(self, from_choose = 0, from_select = 0, is_this_for_image = 0):
        if self.ru_label != None and from_select == 1:
            self.ru_label.grid(rows = 2, column = 0)
        if self.user_to_whom_message_is_to_sent != None and from_select == 1:
            self.user_to_whom_message_is_to_sent.grid(rows = 2, column = 1)
            if from_select == 1:
                self.user_to_whom_message_is_to_sent.current(0)
        if self.rg_label != None and from_select == 1:
            self.rg_label.grid(rows = 3, column = 0)
        if self.group_to_which_message_is_to_be_sent != None and from_select == 1:
            self.group_to_which_message_is_to_be_sent.grid(rows = 3, column = 1)
            if from_select == 1:
                self.group_to_which_message_is_to_be_sent.current(0)
        if self.it_label != None and from_select == 1:
            self.it_label.grid(rows = 4, column = 0)
        if self.image_or_text != None and from_select == 1:
            self.image_or_text.grid(rows = 4, column = 1)
            if from_select == 1:
                self.image_or_text.current(1)
        if self.button_choose != None and from_select == 1:
            self.button_choose.grid(rows = 5, column = 0, columnspan = 2)
        if self.mt_label != None and from_choose == 1:
            self.mt_label.grid(rows = 6, column = 0)
        if self.messagebox != None and from_choose == 1 and is_this_for_image == 0:
            self.messagebox.grid(rows = 6, column = 1)
        if self.image_selector_button != None and from_choose == 1 and is_this_for_image == 1:
            self.image_selector_button.grid(rows = 6, column = 1)
        if self.sender_button != None and from_choose == 1:
            self.sender_button.grid(rows = 7, column = 0, columnspan = 2)

# Class for User
class User:
    
    # Constructor
    def __init__(self, user_id, contacts):
        self.user_id = user_id
        self.contacts = contacts
        self.in_these_groups = []
        self.received_messages = []  

# Class for Group
class Group:

    # Constructor
    def __init__(self, group_id):
        self.group_id = group_id
        self.members = []

    # Utility Function to add members to a group
    def add_members(self, member):
        self.members.append(member)
        member.in_these_groups.append(self)

# Function that reads the 'social-network.txt' file and returns a dictionary of users and groups
def file_reader():
    file = open("social_network.txt", "r")
    users = {}
    groups = {}
    flag = None
    for line in file.readlines():
        if '#users' in line:
            flag = 1
            continue
        elif '#group' in line:
            flag = 2
            continue
        
        line = line.replace('<', '')
        line = line.replace('>', '')
        line = line.replace('\n', '')
        input = line.split(': ')
        input[1] = input[1].split(', ')

        if flag == 1:
            users[input[0]] = input[1]
        else:
            groups[input[0]] = input[1]
    file.close()

    for i in users.keys():
        for j in users[i]:
            if j not in users.keys():
                users[i].remove(j)
                print("Invalid contact " + str(j) + " found in the contact list of user " + str(i) + ". It has not been added.")
            if j == i:
                users[i].remove(j)
                print("A user cannot be its own contact. Hence user number " + str(j) + " has not been added to its own contact list")
    
    for i in groups.keys():
        for j in groups[i]:
            if j not in users.keys():
                groups[i].remove(j)
                print("Invalid contact " + str(j) + " found in the member list of group " + str(i) + ". It has not been added.")
    return users, groups

# Function to quit the application
def quit():
    root.quit()

# Function to quit the pop up window
def exit(root_):
    root_.destroy()

# Main Function
if __name__ == '__main__':
    users, groups = file_reader()
    users_obj = {}
    groups_obj = {}

    # Adding objects of User and Group type in the dictionaries
    for i in users.keys():
        users_obj[i] = User(i, users[i])
    for i in groups.keys():
        groups_obj[i] = Group(i)
        for j in groups[i]:
            groups_obj[i].add_members(users_obj[j])

    # If there are pre-existing messages, then they are loaded
    if path.exists("messages.txt"):
        f = open("messages.txt", "r")
        while True:
            line1 = f.readline()
            line2 = f.readline()
            if not line2:
                break 
            users_obj[line2[:-1]].received_messages.append(line1[:-1])

    # Creates the root window
    root = Tk()

    #Creates the title for the root window
    root.title("Mini Whatsapp")

    # Doesn't allow the user to reshape the main window
    root.resizable(0,0)
    button = Button(root, text = 'EXIT', command = quit, width = 15, height = 3)
    button.pack(pady=10)

    # Creating the objects of the Classes to implement them
    contacts_disp = Display_Contacts()
    groups_disp = Display_Groups()
    message_disp = Display_Messages()
    send_message = Send_Messages()

    # The mainloop that keeps the program running
    root.mainloop()