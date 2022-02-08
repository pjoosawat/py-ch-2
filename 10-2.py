try:
    w = int(input("ป้อนน้ำหนัก"))
    h = int(input("ป้อนส่วนสูง"))
    bmi = w / ((h/100)**2)
except:
    print("error")

    
else:
    print("คำตอบ", bmi)
    
    
    
    
