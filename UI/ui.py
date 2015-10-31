from Tkinter import *
import tkMessageBox
import MySQLdb

fields = 'Title', 'Body'

def findAllTags():
   db = MySQLdb.connect("localhost","root","ashu","stack_overflow" )
   cursor = db.cursor()
   cursor.execute("select name from tag;")
   data = cursor.fetchall()
   db.close()
   global tags
   tags = [element for tupl in data for element in tupl]
   tags.append("None")
   print tags

def check():
    v = [tag1_val.get(),tag2_val.get(),tag3_val.get(),tag4_val.get(),tag5_val.get()]
    for x in range(0, len(v)):
        for y in range(0, len(v)):
            if v[x]==v[y] and x!=y and v[x]!="None":
                return 1
    return 0

def fetch(entries):
   v = 0
   for entry in entries:
      field = entry[0]
      text  = entry[1].get()
      print('%s: "%s"' % (field, text))
      if text is "":
          tkMessageBox.showinfo("Error","Title or Body missing !")
          status_val.set("Always fill Title or Body before querying...")
          break
      else:
          status_val.set(field +" is filled.")
          v+= 1
   if v==2:
       if tag1_val.get() == "Tag1" or tag2_val.get() == "Tag2" or tag3_val.get() == "Tag3" or tag4_val.get() == "Tag4" or tag5_val.get() == "Tag5":
          tkMessageBox.showinfo("Error","Tags are not set !")
          status_val.set("You can choose a tag as 'None' but Fill all tags...")
       elif check()==1:
          tkMessageBox.showinfo("Error","Tags can't be same!")
          status_val.set("Tags need to be pairwise distinct")
       else:
          print "Tags :",tag1_val.get(),tag2_val.get(),tag3_val.get(),tag4_val.get(),tag5_val.get()
          status_val.set("Finding duplicates...")
          T['state'] = 'normal'
          s = "Query >>> \n> Title : "+entries[0][1].get()+"\n> Body : "+entries[1][1].get()+"\n> Tag1 : "+tag1_val.get()+"\n> Tag2 : "+tag2_val.get()+"\n> Tag3 : "+tag3_val.get()+"\n> Tag4 : "+tag4_val.get()+"\n> Tag5 : "+tag5_val.get()+" \n--------------------------------------------\n"
          T.insert('1.0',s)
          status_val.set("Got the Reponse...")
          T.insert('1.0',"Response >>> Done !\n") #showing the response
          T['state'] = 'disable'

def makeform(root, fields):
   topframe = Frame(root)
   topframe.pack(side=TOP, fill=BOTH)
   global entries
   entries = []
   for field in fields:
      row = Frame(topframe)
      lab = Label(row, width=8, text=field, anchor='w')
      ent = Entry(row)
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT, fill=X)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries.append((field, ent))

   lab = Label(topframe, width=9, text=" Tags", anchor='w')
   lab.pack(side=LEFT)
   global listbox
   scrollbar = Scrollbar(topframe, orient=VERTICAL)
   listbox = Listbox(topframe, yscrollcommand=scrollbar.set)
   for item in tags:
      listbox.insert(END, item)

   scrollbar.config(command=listbox.yview)
   scrollbar.pack(side=RIGHT, fill=Y)
   listbox.pack(side=RIGHT, fill=BOTH, expand=1)
   listbox.bind("<<ListboxSelect>>", removeChoice)

   bottomframe = Frame(root)
   bottomframe.pack(side=BOTTOM)
   topframe2 = Frame(bottomframe)
   topframe2.pack(side=TOP)
   global var1, var2, var3, var4, var5
   global tag1_val, tag2_val, tag3_val, tag4_val, tag5_val
   tag1_val = StringVar()
   tag1_val.set("Tag1")
   tag2_val = StringVar()
   tag2_val.set("Tag2")
   tag3_val = StringVar()
   tag3_val.set("Tag3")
   tag4_val = StringVar()
   tag4_val.set("Tag4")
   tag5_val = StringVar()
   tag5_val.set("Tag5")
   var1 = IntVar()
   var2 = IntVar()
   var3 = IntVar()
   var4 = IntVar()
   var5 = IntVar()
   tag1 = Checkbutton(topframe2, textvariable=tag1_val,  variable=var1, command=checked1)
   tag1.pack(side=LEFT)
   tag2 = Checkbutton(topframe2, textvariable=tag2_val,  variable=var2, command=checked2)
   tag2.pack(side=LEFT)
   tag3 = Checkbutton(topframe2, textvariable=tag3_val,  variable=var3, command=checked3)
   tag3.pack(side=LEFT)
   tag4 = Checkbutton(topframe2, textvariable=tag4_val,  variable=var4, command=checked4)
   tag4.pack(side=LEFT)
   tag5 = Checkbutton(topframe2, textvariable=tag5_val,  variable=var5, command=checked5)
   tag5.pack(side=LEFT)

   return entries

def checked1(*event):
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    status_val.set("Tag1 checked...")

def checked2(*event):
    var1.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    status_val.set("Tag2 checked...")

def checked3(*event):
    var1.set(0)
    var2.set(0)
    var4.set(0)
    var5.set(0)
    status_val.set("Tag3 checked...")

def checked4(*event):
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var5.set(0)
    status_val.set("Tag4 checked...")

def checked5(*event):
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    status_val.set("Tag5 checked...")

def removeChoice(*event):
    print listbox.get(listbox.curselection()[0])
    if var1.get()==1:
        tag1_val.set(listbox.get(listbox.curselection()[0]))
        status_val.set("Tag1 set!")
    elif var2.get()==1:
        tag2_val.set(listbox.get(listbox.curselection()[0]))
        status_val.set("Tag2 set!")
    elif var3.get()==1:
        tag3_val.set(listbox.get(listbox.curselection()[0]))
        status_val.set("Tag3 set!")
    elif var4.get()==1:
        tag4_val.set(listbox.get(listbox.curselection()[0]))
        status_val.set("Tag4 set!")
    elif var5.get()==1:
        tag5_val.set(listbox.get(listbox.curselection()[0]))
        status_val.set("Tag5 set!")
    else:
        tkMessageBox.showinfo("Error", "Check a Tag first!")
        status_val.set("Select a Tag's checkbox and then click on any list element to assign it...")

def refresh():
    entries[0][1].delete(0,'end')
    entries[1][1].delete(0,'end')
    tag1_val.set("Tag1")
    tag2_val.set("Tag2")
    tag3_val.set("Tag3")
    tag4_val.set("Tag4")
    tag5_val.set("Tag5")
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    status_val.set("Refreshed...")
    T['state'] = 'normal'
    T.insert('1.0', "-------------------XX---Refreshed---XX-------------------\n\n")
    T['state'] = 'disable'

if __name__ == '__main__':

   findAllTags()

   root = Tk()
   root.title("StackOverflow Questions")
   topframe = Frame(root, bg="green")
   topframe.pack(side=TOP, fill=BOTH)
   ents = makeform(topframe, fields)
   root.bind('<Return>', (lambda event, e=ents: fetch(e)))

   bottomframe = Frame(root)
   bottomframe.pack(side=BOTTOM, fill=BOTH)
   topframe2 = Frame(bottomframe)
   topframe2.pack(side=TOP, fill=BOTH)
   bottomframe2 = Frame(bottomframe)
   bottomframe2.pack(side=BOTTOM, fill=BOTH)
   topframe3 = Frame(bottomframe2)
   topframe3.pack(side=TOP, fill=BOTH)
   bottomframe3 = Frame(bottomframe2)
   bottomframe3.pack(side=BOTTOM, fill=BOTH)

   global T
   scrollbar = Scrollbar(topframe2, orient=VERTICAL)
   T = Text(topframe2, height=15, width=100, yscrollcommand=scrollbar.set)
   scrollbar.config(command=T.yview)
   scrollbar.pack(side=RIGHT, fill=Y)
   T.pack(side=TOP, fill=BOTH)
   T.insert(END, "---Response History---")
   T.config(state=DISABLED)

   b2 = Button(bottomframe2, text='Refresh', command=refresh)
   b2.pack(side=RIGHT, padx=5, pady=5)
   b1 = Button(bottomframe2, text='Find Duplicate', command=(lambda e=ents: fetch(e)))
   b1.pack(side=RIGHT, padx=5, pady=5)
   global status_val
   status_val = StringVar()
   status_val.set("Status Bar...")
   status = Label(bottomframe3, textvariable=status_val, bd=1, relief=SUNKEN, anchor=W)
   status.pack(side=BOTTOM, fill=X)
   root.resizable(0,0)
   root.mainloop()
