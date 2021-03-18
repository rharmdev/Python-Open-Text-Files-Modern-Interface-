import main 
class functions():
    def FS():
        root.wm_attributes('-fullscreen','true')
        buttons.But2.place_forget()
        buttons.But5.place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)


    def  items():
        But1.place_forget()
        But3.place(rely=1.0, relx=0, x=0, y=0, anchor=SW)
        entry1.place(rely=0.25, relx=0.5, x=0, y=0, anchor="center", height=100, width=200)
        But4.place(rely=0.5, relx=0.5, x=0, y=0, anchor="center")

    def entry():
        textenter = entry1.get()
        f = open("numbers.txt", "w")
        f.write(textenter)
        f.close()
        os.startfile("numbers.txt", 'open')

    def window():
        root.wm_attributes('-fullscreen','false')
        But5.place_forget()
        But2.place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)
    
    def close_window():
        root.destroy()



functions()