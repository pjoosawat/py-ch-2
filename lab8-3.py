def triangle():
    b = int(base.get())
    h = int(high.get())
    a = 1/2*b*h
    messagebox.showinfo("พื้นที่สามเหลี่ยม" , "คำตอบ %.2f" % a)
    area.set(a)
    
from tkinter import *
main = Tk()
main.geometry("800x600")
main.title("โปรแกรมหาพื้นที่สามเหลี่ยม โดย อนันท์สิทธิ์ จูสวัสดิ์")
base = StringVar()
high = StringVar()
area = StringVar()

lb1 = Label(main , text="รับค่าฐาน: ", font=("FreesiaUPC",24))
lb1.place(x = 20, y = 20)
tb1 = Entry(main, textvariable = base)
tb1.place(x = 200, y = 30, width = 200, height=30)

lb2 = Label(main , text="รับค่าสูง: ", font=("FreesiaUPC",24))
lb2.place(x = 20, y = 70)
tb2 = Entry(main, textvariable = high)
tb2.place(x = 200, y = 75, width = 200, height=30)

btn = Button(main, text="คำนวณ", font=("FreesiaUPC",24), command=triangle)
btn.place(x=200,y=130)

lb3 = Label(main , text="คำตอบ: ", font=("FreesiaUPC",24))
lb3.place(x = 20, y = 200)

lb4 = Label(main ,bg="#556699", font=("FreesiaUPC",24), textvariable=area)
lb4.place(x = 200, y = 200)

main.mainloop()





