from tkinter import *
import os
import csv
import time
from tkinter import filedialog
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
count,c=0,0
creds = 'tempfile.temp' 

def mail():
    def attach():
        global count
        count+=1
        root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",
                                        filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
       
        file=Label(root,text=root.filename)
        file.grid(row=7,column=0,sticky=W)

    def Pass():
        pass
    def Sendmail():
        global count
        global c
        msg=MIMEMultipart()
        msg['From']='lemneye.py@gmail.com'      
        msg['To']= Toe.get()    
        msg['Subject']= Subjecte.get()
        
        body = texte.get("1.0","end-1c")
        msg.attach(MIMEText(body,'plain'))
        if count>0:
            filename = root.filename
            attachment=open(filename,'rb')
            part=MIMEBase('application','octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',"attachment; filename="+filename)
            msg.attach(part)
        else:
            pass
        text=msg.as_string()
        mail=smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login("lemneye.py@gmail.com","Mneyatou@p1")
        
        try:
            mail.sendmail("lemneye.py@gmail.com",msg['To'],text)
            c+=1
            print('email sent')
        except:
            print ('error sending email')

        mail.quit()
        root.destroy()
        if c >= 1:
            
            r=Tk()
            r.title(':D')
            r.iconbitmap(r'mail.ico')
            r.geometry('150x50')
            rlbl=Label(r,text='\n[+] Email sent')
            rlbl.pack()
            r.mainloop()

        else:
            r=Tk()
            r.title(':D')
            r.iconbitmap(r'mail.ico')
            r.geometry('150x50')
            rlbl=Label(r,text='\n[!] Error Sending Email')
            rlbl.pack()
            r.mainloop()
        



    root=Tk()
    root['bg']="#191970"
    root['pady']=140
    root['padx']=130
    root.title('New Message')
    root.iconbitmap(r'mail.ico')
    To=Label(root,text="To:",background='pink')
    Subject=Label(root,text="Subject:")
    text=Label(root,text="Message:",background='pink')
    To.grid(row=1,column=0,sticky=W,pady=20)
    Subject.grid(row=2,column=0,sticky=W)
    text.grid(row=3,column=0,sticky=NW)

    Toe=Entry(root,width=67)
    Subjecte=Entry(root,width=67)
    texte=Text(root,width=87,height=8)
    Toe.grid(row=1,column=1,sticky=W)
    Subjecte.grid(row=2,column=1,sticky=W,pady=20)
    texte.grid(row=3,column=1,sticky=W,pady=30)

    attach=Button(root,text="Attach",relief=GROOVE,command=attach)
    attach.grid(row=6,column=2,sticky=W)
    send=Button(root,text="Send",relief=GROOVE,command=Sendmail,padx=30)
    send.grid(row=6,column=1,sticky=W)
    file=Label(root,text='',background="#191970")
    file.grid(row=5,column=0,sticky=W)
    root.geometry('900x570')
    root.mainloop()
   
def send():
    global ro
    ro=Tk()
    ro['bg']="#191970"
    ro['pady']=70
    ro['padx']=105
    ro.title('Send Message')
    ro.iconbitmap(r'mail.ico') 
    ro.geometry('400x200')
    new=Button(ro,text='New Message',relief=GROOVE,command=mail,background='pink')
    new.grid(row=1,column=0,sticky=N)
    new=Button(ro,text='Log Out',relief=GROOVE,command=logout)
    new.grid(row=1,column=2,sticky=N)
    ro.mainloop()
def logout():
    ro.destroy()
    login()
    
def Signup():   
    global pwordE  
    global nameE
    global roots
    rootA.destroy()
    roots=Tk() 
    roots['bg']="#191970"
    roots['pady']=70
    roots['padx']=130
    roots.title("Signup")   
    roots.iconbitmap(r'mail.ico')
    #intruction=Label(roots,text='Please Enter new Credidentials\n',background='pink') 
    #intruction.grid(row=0,column=0,sticky=E)  

    nameL=Label(roots,text='Username: ',background='pink') 
    pwordL=Label(roots,text='Password: ')
    nameL.grid(row=1,column=0,sticky=W) 
    pwordL.grid(row=2,column=0,sticky=W)
    
    nameE=Entry(roots)  
    pwordE=Entry(roots,show='*')   
    nameE.grid(row=1,column=1)
    pwordE.grid(row=2,column=1)
    
    signupButton=Button(roots,text='Signup',relief=GROOVE,command=FSSignup,pady=10,padx=20)
    signupButton.grid(columnspan=3,sticky=W,column=1)
    roots.mainloop()    

def FSSignup():
    with open(creds,'a') as f:   
        
        f.write(nameE.get())     
        f.write(',')
        f.write(pwordE.get())   
        f.write('\n')
        f.close()  
    roots.destroy()
    login()     

def login():
    global nameEL
    global pwordEL
    global rootA
    rootA=Tk()
    rootA['bg']="#191970"
    rootA['pady']=70
    rootA['padx']=130
    rootA.title('Mailer')
    rootA.iconbitmap(r'mail.ico')
    intruction=Label(rootA,text='Please Login\n',padx=10,pady=1)
    intruction.grid(sticky=E)

    nameL=Label(rootA,text='Username: ',background='pink')
    pwordL=Label(rootA,text='Password: ')
    nameL.grid(row=1,sticky=W)
    pwordL.grid(row=2,sticky=W)

    nameEL=Entry(rootA)
    pwordEL=Entry(rootA,show='*')
    nameEL.grid(row=1,column=1)
    pwordEL.grid(row=2,column=1)

    loginB=Button(rootA,text='Login',relief=GROOVE,command=CheckLogin,padx=76)
    loginB.grid(columnspan=2,sticky=W,column=1)
    loginB=Button(rootA,text='Signup',relief=GROOVE,command=Signup,padx=72)
    loginB.grid(columnspan=2,sticky=W,column=1)
    
    rmuser=Button(rootA,text='Delete User',fg='red',relief=GROOVE,command=DelUser)
    rmuser.grid(column=2,sticky=W)
    rootA.mainloop()
    
    
def CheckLogin():
    global ro
    with open(creds) as f:
        data=csv.reader(f)
        for line in data:
            try:
                uname=line[0]
                pword=line[1]
                if nameEL.get() == uname and pwordEL.get() == pword:
                    rootA.destroy()
                    send()
                                        
            except IndexError:
                pass
        else:
            #rootA.destroy()
            r=Tk()
            r.title(':D')
            r.iconbitmap(r'mail.ico')
            r.geometry('150x50')
            rlbl=Label(r,text='\n[!] Invalid Login')
            rlbl.pack()
            r.mainloop()
            login()
                    
def DelUser():
    os.remove(creds)
    rootA.destroy()
    Signup()

if os.path.isfile(creds):
    login()
else:
    Signup()
