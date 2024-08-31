import tkinter as tk
from PIL import Image, ImageTk
from UnityTab import Inventory


class TkinterTab:
    def mainloop(self):
        print("###########")
        print("tk loaded")
        root = tk.Tk()
        root.title("Inventory")
        root.geometry("1100x200")
        root.resizable(False, False)

        label = tk.Label(root, text="Minecraft Iventory", width=70, height=5, fg="black")
        label.pack()
        label.place(x=230, y=0)

        img1 = Image.open("assets/button/grassside.png")
        photo1 = ImageTk.PhotoImage(img1)
        self.button1 = tk.Button(root, overrelief="solid", width=100, height=100, command=self.function1,
                                 repeatdelay=1000, repeatinterval=100, image=photo1)
        self.button1.pack()
        self.button1.place(x=0, y=100)

        img2 = Image.open("assets/button/dirtside.png")
        photo2 = ImageTk.PhotoImage(img2)
        self.button2 = tk.Button(root, overrelief="solid", width=100, height=100, command=self.function2,
                                 repeatdelay=1000, repeatinterval=100, image=photo2)
        self.button2.pack()
        self.button2.place(x=100, y=100)

        img3 = Image.open("assets/button/buttonside.png")
        photo3 = ImageTk.PhotoImage(img3)
        self.button3 = tk.Button(root, overrelief="solid", width=100, height=100, command=self.function3,
                                 repeatdelay=1000, repeatinterval=100, image=photo3)
        self.button3.pack()
        self.button3.place(x=200, y=100)

        img4 = Image.open("assets/button/Ironblockside.png")
        photo4 = ImageTk.PhotoImage(img4)
        self.button4 = tk.Button(root, overrelief="solid", width=100, height=100, command=self.function4,
                                 repeatdelay=1000, repeatinterval=100, image=photo4)
        self.button4.pack()
        self.button4.place(x=300, y=100)

        img5 = Image.open("assets/button/redstonelampside.png")
        photo5 = ImageTk.PhotoImage(img5)
        self.button5 = tk.Button(root, overrelief="solid", width=100, height=100, command=self.function5,
                                 repeatdelay=1000, repeatinterval=100, image=photo5)
        self.button5.pack()
        self.button5.place(x=400, y=100)

        img6 = Image.open("assets/button/redstoneside.png")
        photo6 = ImageTk.PhotoImage(img6)
        self.button6 = tk.Button(root, overrelief="solid", width=100, height=100, command=self.function6,
                                 repeatdelay=1000, repeatinterval=100, image=photo6)
        self.button6.pack()
        self.button6.place(x=500, y=100)

        img7 = Image.open("assets/button/redstoneblockside.png")
        photo7 = ImageTk.PhotoImage(img7)
        self.button7 = tk.Button(root, overrelief="solid", width=100, height=100, command=self.function7,
                                 repeatdelay=1000, repeatinterval=100, image=photo7)
        self.button7.pack()
        self.button7.place(x=600, y=100)

        img8 = Image.open("assets/button/torchside.png")
        photo8 = ImageTk.PhotoImage(img8)
        self.button8 = tk.Button(root, overrelief="solid", width=100, height=100, command=self.function8,
                                 repeatdelay=1000, repeatinterval=100, image=photo8)
        self.button8.pack()
        self.button8.place(x=700, y=100)

        img9 = Image.open("assets/button/repeaterside.png")
        photo9 = ImageTk.PhotoImage(img9)
        self.button9 = tk.Button(root, overrelief="solid", width=100, height=100, command=self.function9,
                                 repeatdelay=1000, repeatinterval=100, image=photo9)
        self.button9.pack()
        self.button9.place(x=800, y=100)

        img10 = Image.open("assets/button/stoneside.png")
        photo10 = ImageTk.PhotoImage(img10)
        self.button10 = tk.Button(root, overrelief="solid", width=100, height=100, command=self.function10,
                                  repeatdelay=1000, repeatinterval=100, image=photo10)
        self.button10.pack()
        self.button10.place(x=900, y=100)

        img11 = Image.open("assets/button/switchside.png")
        photo11 = ImageTk.PhotoImage(img11)
        self.button11 = tk.Button(root, overrelief="solid", width=100, height=100, command=self.function11,
                                  repeatdelay=1000, repeatinterval=100, image=photo11)
        self.button11.pack()
        self.button11.place(x=1000, y=100)
        root.mainloop()

    def function1(self):
        Inventory.selected = 1
        print("selected1")

    def function2(self):
        Inventory.selected = 2
        print("selected2")

    def function3(self):
        Inventory.selected = 3
        print("selected3")

    def function4(self):
        Inventory.selected = 4
        print("selected4")

    def function5(self):
        Inventory.selected = 5
        print("selected5")

    def function6(self):
        Inventory.selected = 6
        print("selected6")

    def function7(self):
        Inventory.selected = 7
        print("selected7")

    def function8(self):
        Inventory.selected = 8
        print("selected8")

    def function9(self):
        Inventory.selected = 9
        print("selected9")

    def function10(self):
        Inventory.selected = 10
        print("selected10")

    def function11(self):
        Inventory.selected = 11
        print("selected11")
