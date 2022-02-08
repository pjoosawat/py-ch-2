def cal():
    r = int(tb1.get())
    circle = (3.14)*r*r
    messagebox.showinfo("พื้นที่วงกลม","ผลลัพธ์ %.2f" % circle)
    result.set(circle)
    

from tkinter import *
window = Tk()
window.geometry("800x500")
window.title("โดย อนันท์สิทธิ์ จูสวัสดิ์")

result = StringVar()

lb = Label(window , text="ยินดีต้อนรับเข้าสู่ python",font=("FreesiaUPC",24))

lb.place(x=50,y=10)
#lb.pack()
lb2 = Label(window , text="รับค่ารัศมี",font=("FreesiaUPC",18))
lb2.place(x=50,y=80)

tb1 = Entry(window)
tb1.place(x=200, y=90, height=30)

lb3 = Label(window , text="ผลลัพธ์",font=("FreesiaUPC",18))
lb3.place(x=50,y=120)

tb2 = Entry(window, textvariable = result)
tb2.place(x=200, y=130, height=30)

btn = Button(window,text="คำนวณ",font=("FreesiaUPC",24), command=cal)
btn.place(x=400, y=100, height=30)

window.mainloop()





