def Checkgrade():
    score=int(tb1.get())
    midterm=int(tb2.get())
    final=int(tb3.get())
    love = int(tb4.get())
    total=score+midterm+final+love
    answer.set(total)
    

from tkinter import*
main = Tk()
main.geometry("800x600")
main.title("โปรแกรมเช็คเกรด โดย อนันท์สิทธิ์ จูสวัสดิ์")
answer=StringVar()

lb1 = Label(main , text="คะแนนเก็บ ", font=("Tahoma",16))
lb1.place(x = 20, y = 50)
tb1 = Entry(main)
tb1.place(x = 200, y = 50, width = 200, height=30)

lb2 = Label(main , text="คะแนนกลางภาค ", font=("Tahoma",16))
lb2.place(x = 20, y = 100)
tb2 = Entry(main)
tb2.place(x = 200, y = 100, width = 200, height=30)


lb3 = Label(main , text="คะแนนปลายภาค ", font=("Tahoma",16))
lb3.place(x = 20, y = 150)
tb3 = Entry(main)
tb3.place(x = 200, y = 150, width = 200, height=30)


lb4 = Label(main , text="จิตพิสัย ", font=("Tahoma",16))
lb4.place(x = 20, y = 200)
tb4 = Entry(main)
tb4.place(x = 200, y = 200, width = 200, height=30)

lb5 = Label(main , text="คำตอบ ", font=("Tahoma",24))
lb5.place(x = 20, y = 300)


lb6 = Label(main ,  font=("Tahoma",16),textvariable=answer)
lb6.place(x = 281, y = 300)

btn = Button(main, text="คำนวณ", font=("Tahoma",16),command=Checkgrade)
btn.place(x=450,y=50)

main.mainloop()










