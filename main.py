from tkinter import StringVar, Tk, Label, filedialog, ttk, messagebox
import getpass
import threading
import pytesseract
import cv2
import os
import csv
import imghdr
import datetime
from forex_python.converter import CurrencyRates
from textblob import TextBlob
from get_info import get_info
from colours import colourcheck

results = [0,0,0]

pytesseract.pytesseract.tesseract_cmd = r"Tesseract-OCR\tesseract.exe"

try:
    with open("data/date.txt",'r') as data:
        last_time = data.readlines()
    data.close()
    placeflag = True
except:
    last_time = [""]
    placeflag = False

root = Tk()
root.title("Converter")
root.iconbitmap("resources/bill.ico")    

root.geometry('350x180')

l1 = Label(root, text="Enter the path to your image here, or browse for a file:", width=40)
l1.place(x=33,y=10)


l2 = Label(root, text="Click Go to convert!")
l2.place(x=60, y=77)

l_up = Label(root, text="Rates last updated on " + last_time[0])
if placeflag == True:
    l_up.place(x=50,y=150)


e = ttk.Entry(root, width=35)
e.place(x=31,y=40)
e.insert(0, "")

global menu
menu = StringVar()
menu.set("CAD")

drop = ttk.OptionMenu(root,menu,"CAD","USD","MXN",'EUR','GBP','NOK','SEK','INR','CHF','AUD','NZD','HKD','SGD')

drop.place(x=15,y=118)

def csv_integrity_check():
    baseline = ['USD', 'CAD', 'MXN', 'EUR', 'GBP', 'NOK', 'SEK', 'SGD', 'AUD', 'NZD', 'HKD', 'CHF', 'INR']

    try:
        f = open('data/conv.csv')
    except:
        return 1
    csv_f = csv.reader(f)

    data = list(csv_f)
    f.close()
    origin =[]
    try:
        for d in data:
            origin.append(d[0])
    except:
        return 1

    if origin != baseline:
        return 1


def gui_update():
    global ut
    global lab2

    ut = threading.Thread(target=update_rates)
    ut.daemon = True
    schedule_check_gui(ut) 
    ut.start()

    update.destroy()
    drop.destroy()
    go.destroy()
    l1.config(text='Updating Rates...',font=100)
    l1.place(x=0,y=20)
    l2.destroy()
    l_up.destroy()
    e.destroy()
    lab2 = ttk.Button(text="Abort",command=root.destroy)
    lab2.place(x=143,y=85)
    Browse.destroy()
    
    
def schedule_check_gui(ut):
    root.after(100, check_if_done_gui, ut)

def check_if_done_gui(ut):
    if not ut.is_alive():
        l1.config(text="Updating rates complete!")
        lab2.config(text="Done")
        lab2.place(x=143,y=95)
    else:
        schedule_check_gui(ut)

def update_rates():
    c = CurrencyRates()

    f = open('data/conv.csv')
    csv_f = csv.reader(f)

    rates = list(csv_f)


    for i in rates:
        i[1] = c.convert("USD", i[0], 1.00)


    writer = csv.writer(open('data/conv.csv','w',newline=''))
    writer.writerows(rates)

    now = datetime.datetime.now()
    now = now.strftime("%Y-%m-%d at %H:%M:%S")

    with open("data/date.txt",'w') as file:
        file.write(now)
    file.close()

update = ttk.Button(text="Update Rates", command=gui_update)
update.place(x=250,y=115)

def openbox():
    global filename
    global fn
    e.delete(0,'end')
    filename = filedialog.askopenfilename(initialdir="/Users/" + getpass.getuser() + "/Desktop", title="Select an image:", 
                                         filetypes=(("all files", "*.*"), ("JPEG files", "*.jpg;*.jpeg"), ("png files", "*.png")))
    e.insert(0, filename)
    fn = e.get()
    

def convert_and_handle_gui():
    global t
    global lab1
    global target

    if csv_integrity_check() == 1:
        messagebox.showerror("Error","Rates file is corrupt or does not exist.")
        return

    try:
        img_chk = imghdr.what(fn)
    except:
        messagebox.showerror("Error","Invalid file or no file selected. Only jpeg/jpg and png are supported.")
        return

    if img_chk == "jpeg" or img_chk == "jpg" or img_chk == "png":
        pass
    else:
        messagebox.showerror("Error","Invalid file or no file selected. Only jpeg/jpg and png are supported.")
        return

    target = menu.get()

    t = threading.Thread(target=convert, args = (fn,target))
    t.daemon = True
    schedule_check(t) 
    t.start()

    update.destroy()
    drop.destroy()
    go.destroy()
    l1.config(text='Loading...',font=100)
    l1.place(x=0,y=40)
    l2.destroy()
    l_up.destroy()
    e.destroy()
    lab1 = ttk.Button(text="Abort",command=root.destroy)
    lab1.place(x=143,y=85)
    Browse.destroy()
    
    
def schedule_check(t):
    root.after(100, check_if_done, t)
    
def check_if_done(t):
    if not results[0] == 0:
        l1.destroy()
        lab1.destroy()
        
        if results[0] == 'x' or results[1] == 'x':
            
            lf = Label(root, text="ERROR: Your bill was not dectected\n or was not supported.",font=100)
            lf.place(x=50, y=50)
        else:
            l3 = Label(root, text= "This bill seems to be worth:", font = 50)
            l3.place(x=75, y=20)
            l4 = Label(root, text=str(results[2]) + " " + target)
            l4.config(font=200)
            l4.place(x=125, y=60)
            l5 = Label(root, text="I think your bill is a "+ results[0] +" "+ results[1] +" note.")
            l5.place(x=75, y=100)
    else:
        schedule_check(t)
    
def check(img, conf):
    EM = 1
    text = pytesseract.image_to_string(img, config=conf)
    text = text.replace("\n", "")
    text = text.replace("\x0c", "")
    text = text.replace("", "")
    text = text.lower()
    origin, value, EM = get_info(text)
    if EM == 0:
        return(origin, value, EM)
    
    
    b = TextBlob(text)
    text = b.correct()
    
    origin, value, EM = get_info(text)
    return(origin, value, EM)
    

def check_with_each_model(img, conf, md):
    size = os.path.getsize(img)/1024
    size = round(size, 0)
    
    if 400 <= size <= 2000:
        messagebox.showerror(title="Program Alert",message="[WARNING]: Large image detected. This may take some time.")
    elif size >= 2001:
        messagebox.showerror(title="Program Alert",message="[WARNING]: Very large image detected. The whole process may " +
         " take up to a few minutes.")
    
    img = cv2.imread(img)
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    out = check(img, conf)
    if out[2] == 0:
        return out
    
    se=cv2.getStructuringElement(cv2.MORPH_RECT , (8,8))
    bg=cv2.morphologyEx(img, cv2.MORPH_DILATE, se)
    img=cv2.divide(img, bg, scale=255)
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY |
    cv2.THRESH_OTSU)[1]
    out = check(img, conf)
    img = cv2.bilateralFilter(img,9,75,75)
    
    
    out = check(img, conf)
    if out[2] == 0:
        return out
    
    img = cv2.bitwise_not(img)
   
    out = check(img, conf)
    return out

def do_twice(img):
    
    conf = r'--psm 12 --oem 3 -l custom'

    md = "A"
    out = check_with_each_model(img, conf, md)
    
    if out[2] == 0:
        return out
    
    else:
        
        conf = r'--psm 12 --oem 3 -l eng'
        md = "B"
        out = check_with_each_model(img, conf, md)
        if out[2] == 0:
            return out
        else:
            return("x")
        
def convert_curr(og_amount,og_origin,target):
    f = open('data/conv.csv')
    csv_f = csv.reader(f)

    data = dict(csv_f)

    return(  (float(og_amount) / float(data[og_origin]))   *   float(data[target]))  
    
def convert(img,target):
    
    amount = 0
    
    out = do_twice(img)
    
    if out == "x":
        origin = 'x'
        valuefinal = 'x'
    
    else:
    
        if out[0] == "":
            valuefinal = 'x'
        else:
            origin = out[0]
            value = out[1]
            vfc = colourcheck(origin, img)
            
            valuefinal = vfc
            
            #cases where vfc =/= value but both are not zero are very rare
            #so it is hard to favour one over the other
            
            #could use some work
            
            if origin == "SGP":
                origin = "SGD"
            
            if value == "":
                value = 0
                
            if vfc == 0:
                valuefinal = value
                
            if valuefinal == 0:
                valuefinal = "x"
            
            
            else:
                amount = convert_curr(float(valuefinal),origin,target)
                amount = format(float(amount), ".2f")
                
               
                
    global results        
    results = [origin, valuefinal, amount]
    
       
    
Browse = ttk.Button(root, text="Browse", command=openbox)
Browse.place(x=250,y=38)

go = ttk.Button(root, text="Go!", command=lambda: convert_and_handle_gui())
go.place(x=200,y=75)


root.mainloop()