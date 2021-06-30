from tkinter import *

base = Tk()
base.title("Quiz Game")
base.geometry("800x600")


def exit1():
    exit(0)


def page2():
    base2 = Tk()
    base2.title("Quiz")
    base2.geometry("800x600")

    def sports():
        base3 = Tk()
        base3.title("Quiz Sports")
        base3.geometry("800x600")

        def sports2():
            base4 = Tk()
            base4.title("Quiz Sports")
            base4.geometry("800x600")

            Lb6 = Label(base4, text="1.The Asian Games are normally held every how many years ?", font=("bold", 17),
                        bg="green", fg="white")
            Lb6.place(x=70, y=70)

            Lb7 = Label(base4, text="0", font=17)
            Lb7.place(x=20, y=10)

            i = IntVar()

            op1 = Radiobutton(base4, text="2", variable=i, value=1)
            op1.place(x=140, y=200)

            op2 = Radiobutton(base4, text="3", variable=i, value=2)
            op2.place(x=500, y=200)

            op3 = Radiobutton(base4, text="4", variable=i, value=3)
            op3.place(x=140, y=350)

            op4 = Radiobutton(base4, text="5", variable=i, value=4)
            op4.place(x=500, y=350)

            op5 = Radiobutton(base4, variable=i, value=5)
            op5.place(x=0, y=0)
            op5.select()

            bt7 = Button(base4, text="NEXT", bg="green", fg="white", font=17, height=1, command=sports3)
            bt7.place(x=300, y=500)

            base4.mainloop()

        def sports3():
            base5 = Tk()
            base5.title("Quiz Sports")
            base5.geometry("800x600")

            Lb6 = Label(base5, text="2. Which country is birth place of cricket ?", font=("bold", 17), bg="green",
                        fg="white")
            Lb6.place(x=70, y=70)

            i1 = IntVar()

            op1 = Radiobutton(base5, text="England", font=17, variable=i1, value=1)
            op1.place(x=140, y=200)
            op2 = Radiobutton(base5, text="India", font=17, variable=i1, value=2)
            op2.place(x=500, y=200)
            op3 = Radiobutton(base5, text="USA", font=17, variable=i1, value=3)
            op3.place(x=140, y=350)
            op4 = Radiobutton(base5, text="Australia", font=17, variable=i1, value=4)
            op4.place(x=500, y=350)

            op5 = Radiobutton(base5, variable=i1, value=5)
            op5.place(x=0, y=0)
            op5.select()

            bt7 = Button(base5, text="NEXT", bg="green", fg="white", font=17, height=1, command=sports4)
            bt7.place(x=300, y=500)

            base5.mainloop()

        def sports4():
            base6 = Tk()
            base6.title("Quiz Sports")
            base6.geometry("800x600")

            Lb6 = Label(base6, text="3.Who is known as flying sikh of india ?", font=("bold", 17), bg="green",
                        fg="white")
            Lb6.place(x=70, y=70)

            i = StringVar()

            op1 = Radiobutton(base6, text="Milkha sing", font=17, variable=i, value=1)
            op1.place(x=140, y=200)
            op2 = Radiobutton(base6, text="Usain Bolt", font=17, variable=i, value=2)
            op2.place(x=500, y=200)
            op3 = Radiobutton(base6, text="Sachin Tendulkar", font=17, variable=i, value=3)
            op3.place(x=140, y=350)
            op4 = Radiobutton(base6, text="Sandip Singh", font=17, variable=i, value=4)
            op4.place(x=500, y=350)

            op5 = Radiobutton(base6, variable=i, value=5)
            op5.place(x=0, y=0)
            op5.select()

            bt7 = Button(base6, text="NEXT", bg="green", fg="white", font=17, height=1, command=sports5)
            bt7.place(x=300, y=500)

            base6.mainloop()

        def sports5():
            base7 = Tk()
            base7.title("Quiz Technology")
            base7.geometry("800x600")

            Lb6 = Label(base7, text="4.Which country hosted Cricket World Cup 2019 ", font=("bold", 17), bg="green",
                        fg="white")
            Lb6.place(x=70, y=70)

            i = IntVar()

            op1 = Radiobutton(base7, text="India", font=17, variable=i, value=3)
            op1.place(x=140, y=200)
            op2 = Radiobutton(base7, text="England", font=17, variable=i, value=1)
            op2.place(x=500, y=200)
            op3 = Radiobutton(base7, text="Australia", font=17, variable=i, value=2)
            op3.place(x=140, y=350)
            op4 = Radiobutton(base7, text="Newzeland", font=17, variable=i, value=4)
            op4.place(x=500, y=350)

            op5 = Radiobutton(base7, variable=i, value=5)
            op5.place(x=0, y=0)
            op5.select()

            bt7 = Button(base7, text="NEXT", bg="green", fg="white", font=17, height=1, command=sports6)
            bt7.place(x=300, y=500)

            base7.mainloop()

        def sports6():
            base8 = Tk()
            base8.title("Quiz history")
            base8.geometry("800x600")

            Lb6 = Label(base8, text="5. Hockey is the national sports of", font=("bold", 17), bg="green",
                        fg="white")
            Lb6.place(x=70, y=70)

            i = IntVar()

            op1 = Radiobutton(base8, text="India", font=17, variable=i, value=1)
            op1.place(x=140, y=200)
            op2 = Radiobutton(base8, text="England", font=17, variable=i, value=3)
            op2.place(x=500, y=200)
            op3 = Radiobutton(base8, text="Portugal", font=17, variable=i, value=2)
            op3.place(x=140, y=350)
            op4 = Radiobutton(base8, text="France", font=17, variable=i, value=4)
            op4.place(x=500, y=350)

            op5 = Radiobutton(base8, variable=i, value=5)
            op5.place(x=0, y=0)
            op5.select()

            bt7 = Button(base8, text="NEXT", bg="green", fg="white", font=17, height=1, command=sports7)
            bt7.place(x=300, y=500)

            base8.mainloop()

        def sports7():
            base9 = Tk()
            base9.title("Quiz Sports")
            base9.geometry("800x600")

            over = Label(base9, text="                 QUIZ OVER                 ", font=("bold", 17),
                         bg="green", fg="white")
            over.place(x=200, y=150)
            bt8 = Button(base9, text="QUIT", bg="red", fg="white", font=17, height=1, command=exit1)
            bt8.place(x=325, y=300)

            base9.mainloop()

        Lb4 = Label(base3, text="INSTRUCTIONS", font=("bold", 17))
        Lb4.place(x=80, y=60)

        Lb3 = Label(base3, text="- To start, click the 'Take the Quiz' button.", font=("bold", 15))
        Lb3.place(x=50, y=160)

        Lb5 = Label(base3, text="- Each question carries 1 point.", font=("bold", 15))
        Lb5.place(x=50, y=120)

        bt6 = Button(base3, text="Take the Quiz", bg="Green", fg="White", font=("bold", 15), command=sports2)
        bt6.place(x=330, y=300)

        base3.mainloop()

    def CurrentAffairs():
        base3 = Tk()
        base3.title("Quiz Current Affairs")
        base3.geometry("800x600")

        def currentaffairs2():
            base4 = Tk()
            base4.title("Quiz Current Affairs")
            base4.geometry("800x600")

            Lb6 = Label(base4, text="1. Earth hour day is annually observed on last saturday of which month ?",
                        font=("bold", 17),
                        bg="green", fg="white")
            Lb6.place(x=70, y=70)

            i = IntVar()

            op1 = Radiobutton(base4, text="June", font=17, variable=i, value=2)
            op1.place(x=140, y=200)
            op2 = Radiobutton(base4, text="April", font=17, variable=i, value=3)
            op2.place(x=500, y=200)
            op3 = Radiobutton(base4, text="March", font=17, variable=i, value=1)
            op3.place(x=140, y=350)
            op4 = Radiobutton(base4, text="May", font=17, variable=i, value=4)
            op4.place(x=500, y=350)

            op5 = Radiobutton(base4, variable=i, value=5)
            op5.place(x=0, y=0)
            op5.select()

            bt7 = Button(base4, text="NEXT", bg="green", fg="white", font=17, height=1, command=currentaffairs3)
            bt7.place(x=300, y=500)

            base4.mainloop()

        def currentaffairs3():
            base5 = Tk()
            base5.title("Quiz current affairs")
            base5.geometry("800x600")

            Lb6 = Label(base5, text="2. Which Tech company has entered renewable energy project in india ?",
                        font=("bold", 17), bg="green",
                        fg="white")
            Lb6.place(x=70, y=70)

            i = IntVar()

            op1 = Radiobutton(base5, text="Amazon", font=17, variable=i, value=2)
            op1.place(x=140, y=200)
            op2 = Radiobutton(base5, text="Facebook", font=17, variable=i, value=1)
            op2.place(x=500, y=200)
            op3 = Radiobutton(base5, text="Google", font=17, variable=i, value=3)
            op3.place(x=140, y=350)
            op4 = Radiobutton(base5, text="Microsoft", font=17, variable=i, value=4)
            op4.place(x=500, y=350)

            op5 = Radiobutton(base5, variable=i, value=5)
            op5.place(x=0, y=0)
            op5.select()

            bt7 = Button(base5, text="NEXT", bg="green", fg="white", font=17, height=1, command=currentaffairs4)
            bt7.place(x=300, y=500)

            base5.mainloop()

        def currentaffairs4():
            base6 = Tk()
            base6.title("Quiz current affairs")
            base6.geometry("800x600")

            Lb6 = Label(base6, text="3.Pohela Boisakh is the festival of which state ?", font=("bold", 17), bg="green",
                        fg="white")
            Lb6.place(x=70, y=70)

            i = IntVar()

            op1 = Radiobutton(base6, text="Delhi", font=17, variable=i, value=2)
            op1.place(x=140, y=200)
            op2 = Radiobutton(base6, text="Maharashtra", font=17, variable=i, value=3)
            op2.place(x=500, y=200)
            op3 = Radiobutton(base6, text="Goa", font=17, variable=i, value=4)
            op3.place(x=140, y=350)
            op4 = Radiobutton(base6, text="West Bengal", font=17, variable=i, value=1)
            op4.place(x=500, y=350)

            op5 = Radiobutton(base6, variable=i, value=5)
            op5.place(x=0, y=0)
            op5.select()

            bt7 = Button(base6, text="NEXT", bg="green", fg="white", font=17, height=1, command=currentaffairs5)
            bt7.place(x=300, y=500)

            base6.mainloop()

        def currentaffairs5():
            base7 = Tk()
            base7.title("Quiz Technology")
            base7.geometry("800x600")

            Lb6 = Label(base7, text="4.Who is the author of the book 'Freedom Behind Bars '", font=("bold", 17),
                        bg="green",
                        fg="white")
            Lb6.place(x=70, y=70)

            i = IntVar()

            op1 = Radiobutton(base7, text="Kiran Bedi", font=17, variable=i, value=1)
            op1.place(x=140, y=200)
            op2 = Radiobutton(base7, text="Jawaharlal Nehru", font=17, variable=i, value=3)
            op2.place(x=500, y=200)
            op3 = Radiobutton(base7, text="Nelson Mandela", font=17, variable=i, value=2)
            op3.place(x=140, y=350)
            op4 = Radiobutton(base7, text="Elon musk", font=17, variable=i, value=4)
            op4.place(x=500, y=350)

            op5 = Radiobutton(base7, variable=i, value=5)
            op5.place(x=0, y=0)
            op5.select()

            bt7 = Button(base7, text="NEXT", bg="green", fg="white", font=17, height=1, command=currentaffairs6)
            bt7.place(x=300, y=500)

            base7.mainloop()

        def currentaffairs6():
            base8 = Tk()
            base8.title("Quiz history")
            base8.geometry("800x600")

            Lb6 = Label(base8, text="5.Which latitude passes through the middle of India?", font=("bold", 17),
                        bg="green",
                        fg="white")
            Lb6.place(x=70, y=70)

            i = IntVar()

            op1 = Radiobutton(base8, text="Equator", font=17, variable=i, value=4)
            op1.place(x=140, y=200)
            op2 = Radiobutton(base8, text="Arctic Circle", font=17, variable=i, value=3)
            op2.place(x=500, y=200)
            op3 = Radiobutton(base8, text="Tropic of Cancer", font=17, variable=i, value=1)
            op3.place(x=140, y=350)
            op4 = Radiobutton(base8, text="Tropic of Capricorn", font=17, variable=i, value=2)
            op4.place(x=500, y=350)

            op5 = Radiobutton(base8, variable=i, value=5)
            op5.place(x=0, y=0)
            op5.select()

            bt7 = Button(base8, text="NEXT", bg="green", fg="white", font=17, height=1, command=currentaffairs7)
            bt7.place(x=300, y=500)

            base8.mainloop()

        def currentaffairs7():
            base9 = Tk()
            base9.title("Quiz Sports")
            base9.geometry("800x600")

            over = Label(base9, text="                 QUIZ OVER                 ", font=("bold", 17),
                         bg="green", fg="white")
            over.place(x=200, y=150)
            bt8 = Button(base9, text="QUIT", bg="red", fg="white", font=17, height=1, command=exit1)
            bt8.place(x=325, y=300)

            base9.mainloop()

        Lb4 = Label(base3, text="INSTRUCTIONS", font=("bold", 17))
        Lb4.place(x=80, y=60)

        Lb3 = Label(base3, text="- To start, click the 'Take the Quiz' button.", font=("bold", 15))
        Lb3.place(x=50, y=160)

        Lb5 = Label(base3, text="- Each question carries 1 point.", font=("bold", 15))
        Lb5.place(x=50, y=120)

        bt6 = Button(base3, text="Take the Quiz", bg="Green", fg="White", font=("bold", 15), command=currentaffairs2)
        bt6.place(x=330, y=300)

        base3.mainloop()

    def History():
        base3 = Tk()
        base3.title("Quiz history")
        base3.geometry("800x600")

        def history2():
            base4 = Tk()
            base4.title("Quiz History")
            base4.geometry("800x600")

            Lb6 = Label(base4, text="1. What is birth date of Mahatma Gandhi ?", font=("bold", 17),
                        bg="green", fg="white")
            Lb6.place(x=70, y=70)

            i = IntVar()

            op1 = Radiobutton(base4, text="8-April", font=17, variable=i, value=2)
            op1.place(x=140, y=200)
            op2 = Radiobutton(base4, text="5-May", font=17, variable=i, value=3)
            op2.place(x=500, y=200)
            op3 = Radiobutton(base4, text="2-October", font=17, variable=i, value=1)
            op3.place(x=140, y=350)
            op4 = Radiobutton(base4, text="8-February", font=17, variable=i, value=4)
            op4.place(x=500, y=350)

            op5 = Radiobutton(base4, variable=i, value=5)
            op5.place(x=0, y=0)
            op5.select()

            bt7 = Button(base4, text="NEXT", bg="green", fg="white", font=17, height=1, command=history3)
            bt7.place(x=300, y=500)

            base4.mainloop()

        def history3():
            base5 = Tk()
            base5.title("Quiz Technology")
            base5.geometry("800x600")

            Lb6 = Label(base5, text="2. When was August Kranti pulled back ?", font=("bold", 17), bg="green",
                        fg="white")
            Lb6.place(x=70, y=70)

            i = IntVar()

            op1 = Radiobutton(base5, text="2004", font=17, variable=i, value=2)
            op1.place(x=140, y=200)
            op2 = Radiobutton(base5, text="1234", font=17, variable=i, value=3)
            op2.place(x=500, y=200)
            op3 = Radiobutton(base5, text="1942", font=17, variable=i, value=1)
            op3.place(x=140, y=350)
            op4 = Radiobutton(base5, text="1978", font=17, variable=i, value=4)
            op4.place(x=500, y=350)

            op5 = Radiobutton(base5, variable=i, value=5)
            op5.place(x=0, y=0)
            op5.select()

            bt7 = Button(base5, text="NEXT", bg="green", fg="white", font=17, height=1, command=history4)
            bt7.place(x=300, y=500)

            base5.mainloop()

        def history4():
            base6 = Tk()
            base6.title("Quiz Technology")
            base6.geometry("800x600")

            Lb6 = Label(base6, text="3. When the Jallianwala Bagh Massacre took place ?", font=("bold", 17), bg="green",
                        fg="white")
            Lb6.place(x=70, y=70)

            i = IntVar()

            op1 = Radiobutton(base6, text="13-April-1919", font=17, variable=i, value=1)
            op1.place(x=140, y=200)
            op2 = Radiobutton(base6, text="9-march-1921", font=17, variable=i, value=2)
            op2.place(x=500, y=200)
            op3 = Radiobutton(base6, text="20-september-1879", font=17, variable=i, value=3)
            op3.place(x=140, y=350)
            op4 = Radiobutton(base6, text="27-May-2021", font=17, variable=i, value=4)
            op4.place(x=500, y=350)

            op5 = Radiobutton(base6, variable=i, value=5)
            op5.place(x=0, y=0)
            op5.select()

            bt7 = Button(base6, text="NEXT", bg="green", fg="white", font=17, height=1, command=history5)
            bt7.place(x=300, y=500)

            base6.mainloop()

        def history5():
            base7 = Tk()
            base7.title("Quiz Technology")
            base7.geometry("800x600")

            Lb6 = Label(base7,
                        text="4.Which of the following city was Not developed as Presidency city in colonial India?",
                        font=("bold", 17), bg="green",
                        fg="white")
            Lb6.place(x=70, y=70)

            i = IntVar()

            op1 = Radiobutton(base7, text="Madras", font=17, variable=i, value=3)
            op1.place(x=140, y=200)
            op2 = Radiobutton(base7, text="Agra", font=17, variable=i, value=1)
            op2.place(x=500, y=200)
            op3 = Radiobutton(base7, text="Bombay", font=17, variable=i, value=2)
            op3.place(x=140, y=350)
            op4 = Radiobutton(base7, text="Dellhi", font=17, variable=i, value=4)
            op4.place(x=500, y=350)

            op5 = Radiobutton(base7, variable=i, value=5)
            op5.place(x=0, y=0)
            op5.select()

            bt7 = Button(base7, text="NEXT", bg="green", fg="white", font=17, height=1, command=history6)
            bt7.place(x=300, y=500)

            base7.mainloop()

        def history6():
            base8 = Tk()
            base8.title("Quiz history")
            base8.geometry("800x600")

            Lb6 = Label(base8, text="5.When did Delhi become the capital of British India?", font=("bold", 17),
                        bg="green", fg="white")
            Lb6.place(x=70, y=70)

            i = IntVar()

            op1 = Radiobutton(base8, text="1941", font=17, variable=i, value=4)
            op1.place(x=140, y=200)
            op2 = Radiobutton(base8, text="1880", font=17, variable=i, value=3)
            op2.place(x=500, y=200)
            op3 = Radiobutton(base8, text="1925", font=17, variable=i, value=2)
            op3.place(x=140, y=350)
            op4 = Radiobutton(base8, text="1911", font=17, variable=i, value=1)
            op4.place(x=500, y=350)

            op5 = Radiobutton(base8, variable=i, value=5)
            op5.place(x=0, y=0)
            op5.select()

            bt7 = Button(base8, text="NEXT", bg="green", fg="white", font=17, height=1, command=history7)
            bt7.place(x=300, y=500)

            base8.mainloop()

        def history7():
            base9 = Tk()
            base9.title("Quiz Sports")
            base9.geometry("800x600")

            over = Label(base9, text="                 QUIZ OVER                 ", font=("bold", 17),
                         bg="green", fg="white")
            over.place(x=200, y=150)
            bt8 = Button(base9, text="QUIT", bg="red", fg="white", font=17, height=1, command=exit1)
            bt8.place(x=325, y=300)

            base9.mainloop()

        Lb4 = Label(base3, text="INSTRUCTIONS", font=("bold", 17))
        Lb4.place(x=80, y=60)

        Lb3 = Label(base3, text="- To start, click the 'Take the Quiz' button.", font=("bold", 15))
        Lb3.place(x=50, y=160)

        Lb5 = Label(base3, text="- Each question carries 1 point.", font=("bold", 15))
        Lb5.place(x=50, y=120)

        bt6 = Button(base3, text="Take the Quiz", bg="Green", fg="White", font=("bold", 15), command=history2)
        bt6.place(x=330, y=300)

        base3.mainloop()

    def Technology():
        base3 = Tk()
        base3.title("Quiz Technology")
        base3.geometry("800x600")

        def Technology2():
            base4 = Tk()
            base4.title("Quiz Technology")
            base4.geometry("800x600")

            Lb6 = Label(base4, text="1. Which one is the first search engine in internet ?", font=("bold", 17),
                        bg="green", fg="white")
            Lb6.place(x=70, y=70)

            i = IntVar()

            op1 = Radiobutton(base4, text="Google", font=17, variable=i, value=2)
            op1.place(x=140, y=200)
            op2 = Radiobutton(base4, text="Archie", font=17, variable=i, value=1)
            op2.place(x=500, y=200)
            op3 = Radiobutton(base4, text="Altavista", font=17, variable=i, value=3)
            op3.place(x=140, y=350)
            op4 = Radiobutton(base4, text="Yahoo", font=17, variable=i, value=4)
            op4.place(x=500, y=350)

            op5 = Radiobutton(base4, variable=i, value=5)
            op5.place(x=0, y=0)
            op5.select()

            bt7 = Button(base4, text="NEXT", bg="green", fg="white", font=17, height=1, command=Technology3)
            bt7.place(x=300, y=500)

            base4.mainloop()

        def Technology3():
            base5 = Tk()
            base5.title("Quiz Technology")
            base5.geometry("800x600")

            Lb6 = Label(base5, text="2. No of Bit used by the IPv6 Address ?", font=("bold", 17), bg="green",
                        fg="white")
            Lb6.place(x=70, y=70)

            i = IntVar()

            op1 = Radiobutton(base5, text="256", font=17, variable=i, value=2)
            op1.place(x=140, y=200)
            op2 = Radiobutton(base5, text="32", font=17, variable=i, value=3)
            op2.place(x=500, y=200)
            op3 = Radiobutton(base5, text="64", font=17, variable=i, value=4)
            op3.place(x=140, y=350)
            op4 = Radiobutton(base5, text="128", font=17, variable=i, value=1)
            op4.place(x=500, y=350)

            op5 = Radiobutton(base5, variable=i, value=5)
            op5.place(x=0, y=0)
            op5.select()

            bt7 = Button(base5, text="NEXT", bg="green", fg="white", font=17, height=1, command=Technology4)
            bt7.place(x=300, y=500)

            base5.mainloop()

        def Technology4():
            base6 = Tk()
            base6.title("Quiz Technology")
            base6.geometry("800x600")

            Lb6 = Label(base6, text="3. First Computer virus is known as ?", font=("bold", 17), bg="green",
                        fg="white")
            Lb6.place(x=70, y=70)

            i = IntVar()

            op1 = Radiobutton(base6, text="Rabbit", font=17, variable=i, value=2)
            op1.place(x=140, y=200)
            op2 = Radiobutton(base6, text="Elk cloner", font=17, variable=i, value=3)
            op2.place(x=500, y=200)
            op3 = Radiobutton(base6, text="Creeper virus", font=17, variable=i, value=1)
            op3.place(x=140, y=350)
            op4 = Radiobutton(base6, text="SCA virus", font=17, variable=i, value=4)
            op4.place(x=500, y=350)

            op5 = Radiobutton(base6, variable=i, value=5)
            op5.place(x=0, y=0)
            op5.select()

            bt7 = Button(base6, text="NEXT", bg="green", fg="white", font=17, height=1, command=Technology5)
            bt7.place(x=300, y=500)

            base6.mainloop()

        def Technology5():
            base7 = Tk()
            base7.title("Quiz Technology")
            base7.geometry("800x600")

            Lb6 = Label(base7, text="4.Who founded Apple Computer?", font=("bold", 17), bg="green",
                        fg="white")
            Lb6.place(x=70, y=70)

            i = IntVar()

            op1 = Radiobutton(base7, text="Steve Jobs", font=17, variable=i, value=1)
            op1.place(x=140, y=200)
            op2 = Radiobutton(base7, text="Elk cloner", font=17, variable=i, value=3)
            op2.place(x=500, y=200)
            op3 = Radiobutton(base7, text="Bill gates", font=17, variable=i, value=2)
            op3.place(x=140, y=350)
            op4 = Radiobutton(base7, text="Elon musk", font=17, variable=i, value=4)
            op4.place(x=500, y=350)

            op5 = Radiobutton(base7, variable=i, value=5)
            op5.place(x=0, y=0)
            op5.select()

            bt7 = Button(base7, text="NEXT", bg="green", fg="white", font=17, height=1, command=Technology6)
            bt7.place(x=300, y=500)

            base7.mainloop()

        def Technology6():
            base8 = Tk()
            base8.title("Quiz Technology")
            base8.geometry("800x600")

            Lb6 = Label(base8, text="5.Who founded Tesla Moters", font=("bold", 17), bg="green",
                        fg="white")
            Lb6.place(x=70, y=70)

            i = IntVar()

            op1 = Radiobutton(base8, text="Steve Jobs", font=17, variable=i, value=4)
            op1.place(x=140, y=200)
            op2 = Radiobutton(base8, text="Elk cloner", font=17, variable=i, value=3)
            op2.place(x=500, y=200)
            op3 = Radiobutton(base8, text="Bill gates", font=17, variable=i, value=2)
            op3.place(x=140, y=350)
            op4 = Radiobutton(base8, text="Elon musk", font=17, variable=i, value=1)
            op4.place(x=500, y=350)

            op5 = Radiobutton(base8, variable=i, value=5)
            op5.place(x=0, y=0)
            op5.select()

            bt7 = Button(base8, text="NEXT", bg="green", fg="white", font=17, height=1, command=Technology7)
            bt7.place(x=300, y=500)

            base8.mainloop()

        def Technology7():
            base9 = Tk()
            base9.title("Quiz Sports")
            base9.geometry("800x600")

            over = Label(base9, text="                 QUIZ OVER                 ", font=("bold", 17),
                         bg="green", fg="white")
            over.place(x=200, y=150)
            bt8 = Button(base9, text="QUIT", bg="red", fg="white", font=17, height=1, command=exit1)
            bt8.place(x=325, y=300)

            base9.mainloop()

        Lb4 = Label(base3, text="INSTRUCTIONS", font=("bold", 17))
        Lb4.place(x=80, y=60)

        Lb3 = Label(base3, text="- To start, click the 'Take the Quiz' button.", font=("bold", 15))
        Lb3.place(x=50, y=160)

        Lb5 = Label(base3, text="- Each question carries 1 point.", font=("bold", 15))
        Lb5.place(x=50, y=120)

        bt6 = Button(base3, text="Take the Quiz", bg="Green", fg="White", font=("bold", 15), command=Technology2)
        bt6.place(x=330, y=300)

        base3.mainloop()

    # Main Logic of category

    Lb2 = Label(base2, text="Select category", bg="yellow", fg="blue", width="30", height=3, font=("Timesnewroman", 15))
    Lb2.place(x=250, y=30)

    bt2 = Button(base2, bg="yellow", fg="blue", text="     Sports    ", font=("bold", 15), command=sports)
    bt2.place(x=150, y=250)

    bt3 = Button(base2, bg="yellow", fg="blue", text="Current Affairs", font=("bold", 15), command=CurrentAffairs)
    bt3.place(x=600, y=250)

    bt4 = Button(base2, bg="yellow", fg="blue", text="   Technology  ", font=("bold", 15), command=Technology)
    bt4.place(x=150, y=350)

    bt5 = Button(base2, bg="yellow", fg="blue", text="    History    ", font=("bold", 15), command=History)
    bt5.place(x=610, y=350)

    base2.mainloop()


Lb1 = Label(base, text="Welcome", bg="skyblue", fg="white", width=25, height="2", font="TimesNewRoman")
Lb1.place(x=270, y=50)

str1 = Label(base, text="", bg="green", width=120)
str1.pack()
str2 = Label(base, text="", bg="green", height=120, width=2)
str2.place(x=0, y=0)
str3 = Label(base, text="", bg="green", height=120, width=2)
str3.place(x=780, y=0)
str4 = Label(base, text="", bg="green", width=120)
str4.place(x=20, y=580)

bt1 = Button(base, text="Next", font=("bold", 14), bg="yellow", fg="blue", command=page2)
bt1.place(x=350, y=350)

base.mainloop()