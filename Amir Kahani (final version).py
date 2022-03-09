import tkinter
import json

def GUI():
    u=userbox.get()
    p=passbox.get()
    with open('tkinter.json')as f:
        info=json.load(f)
        if(u in info and info[u]==p):
            win=tkinter.Tk()
            win.title('WELCOME!')
            win.geometry('250x100')
            lbl=tkinter.Label(win , text='      ')
            lbl.grid(column=0 , row=0)
            lbl=tkinter.Label(win , text='      ')
            lbl.grid(column=1 , row=0)
            lbl2=tkinter.Label(win ,text='      ')
            lbl2.grid(column=2 , row=1)
            lbl1=tkinter.Label(win , text='    W E L C O M E    ' , bg='blue', fg='yellow' )
            lbl1.grid(column=3 , row=1 )
            lbl1=tkinter.Label(win , text='         D E A R !          ' , bg='yellow', fg='blue' )
            lbl1.grid(column=3 , row=2 )
            win.mainloop()
        
        else:
            win=tkinter.Tk()
            win.title('New Tab')
            win.geometry('300x50')
            lbl2=tkinter.Label(win , text='         Ohh! an error occured !' , fg='red' )
            lbl2.grid(column=1 , row=1 )
            lbl2=tkinter.Label(win , text='     Please enter your information correctly or SignUp ' , fg='red')
            lbl2.grid(column=1 , row=2 )
            # btn=tkinter.Button(win , text='    Home Page    ' , bg='white', fg='black' , command=homepage )
            # btn.grid(column=1 , row=5)
            win.mainloop()
            
def signup():
    us=u2.get()
    ps=p2.get()
    #minimum=3
    #maximum=10
    AZ={'~','!','@','$','%','^','&','*','<','(',')','+','-'
           ,'/','}','{','[',']','`',',','.','>',';','"','¿','¡','®',
           '™','∆','√','µ','±','°','ß','¥','£','¢','€',''}
    sus=set(us)  
    
    with open ('tkinter.json' ) as f :
        INFO=json.load(f)
        
        if (us=="") and (ps=="") :
            win11=tkinter.Tk()
            win11.title('New Tab')
            win11.geometry('300x50')
            lbl2=tkinter.Label(win11 , text='                     Please enter your user and pass ' , fg='navy')
            lbl2.grid(column=1 , row=1 )
            win11.mainloop()
            
        elif  (sus.intersection(AZ)) :
            winsus=tkinter.Tk()
            winsus.title('New Tab')
            winsus.geometry('250x50')
            lblsus=tkinter.Label(winsus, text='                JUST NUMBERS OR A-Z ' , fg='blue')
            lblsus.grid(column=1 , row=1 )
            winsus.mainloop()
        
            # print('Just NUMBERS or A-Z')
            
        # elif us not in INFO :
        #     if(len(ps<=minimum) and len(ps>=maximum)):
        #         win12=tkinter.Tk()
        #         win12.title('New Tab')
        #         win12.geometry('250x50')
        #         lbl2=tkinter.Label(win12 , text='      Wrong number of letter ' , fg='blue')
        #         lbl2.grid(column=1 , row=1 )
        #         win12.mainloop()
            
            INFO[us]=ps
            with open ('tkinter.json','w') as f:
                json.dump(INFO,f)
                winnew=tkinter.Tk()
                winnew.title('WELCOME!')
                winnew.geometry('250x100')
                lbl=tkinter.Label(winnew , text='      ')
                lbl.grid(column=0 , row=0)
                lbl=tkinter.Label(winnew , text='      ')
                lbl.grid(column=1 , row=0)
                lbl2=tkinter.Label(winnew ,text='      ')
                lbl2.grid(column=2 , row=1)
                lbl1=tkinter.Label(winnew , text='    W E L C O M E    ' , bg='blue', fg='yellow' )
                lbl1.grid(column=3 , row=1 )
                lbl1=tkinter.Label(winnew , text='         D E A R !          ' , bg='yellow', fg='blue' )
                lbl1.grid(column=3 , row=2 )
                winnew.mainloop()
                # print('welcome user')
                
        elif(us in INFO or INFO[us]==ps):
            win11=tkinter.Tk()
            win11.title('New Tab')
            win11.geometry('300x50')
            lbl2=tkinter.Label(win11 , text='                      The username is duplicate ' , fg='blue')
            lbl2.grid(column=1 , row=1 )
            win11.mainloop()
        # elif(len(ps<=minimum) and len(ps>=maximum)):
        #     win12=tkinter.Tk()
        #     win12.title('New Tab')
        #     win12.geometry('250x50')
        #     lbl2=tkinter.Label(win12 , text='      Wrong number of letter ' , fg='blue')
        #     lbl2.grid(column=1 , row=1 )
        #     win12.mainloop()
        # elif(us.isalnum()==True):
        #     win13=tkinter.Tk()
        #     win13.title('New Tab')
        #     win13.geometry('250x50')
        #     lbl2=tkinter.Label(win13, text='      Just NUMBERS or A-Z ' , fg='blue')
        #     lbl2.grid(column=1 , row=1 )
        #     win13.mainloop()
    # else:
    #     print('an error occured ; Try again!')
                   
def welcome():
    uw=u2.get()
    pw=p2.get()
    with open ('tkinter.json' ) as f :
        info=json.load(f) 
    if uw not in info :
        info[uw]=pw
        with open ('tkinter.json','w') as f:
            json.dump(info,f)
            winw=tkinter.Tk()
            winw.title('WELCOME!')
            winw.geometry('250x100')
            lbl=tkinter.Label(winw , text='      ')
            lbl.grid(column=0 , row=0)
            lbl=tkinter.Label(winw , text='      ')
            lbl.grid(column=1 , row=0)
            lbl2=tkinter.Label(winw ,text='      ')
            lbl2.grid(column=2 , row=1)
            lbl1=tkinter.Label(winw , text='    W E L C O M E    ' , bg='blue', fg='yellow' )
            lbl1.grid(column=3 , row=1 )
            lbl1=tkinter.Label(winw , text='         D E A R !          ' , bg='yellow', fg='blue' )
            lbl1.grid(column=3 , row=2 )
            winw.mainloop()
            # print('welcome user')
    else:
        wind=tkinter.Tk()
        wind.title('WELCOME!')
        wind.geometry('250x100')
        lbl=tkinter.Label(wind , text='      ')
        lbl.grid(column=0 , row=0)
        lbl=tkinter.Label(wind , text='      ')
        lbl.grid(column=1 , row=0)
        lbl2=tkinter.Label(wind ,text='      ')
        lbl2.grid(column=2 , row=1)
        lbl1=tkinter.Label(wind , text='   user already exist    ' , bg='blue', fg='yellow' )
        lbl1.grid(column=3 , row=1 )
        lbl1=tkinter.Label(wind , text='Try another accounts' , bg='yellow', fg='blue' )
        lbl1.grid(column=3 , row=2 )
        wind.mainloop()
        # print('user already exist')    

def btn1():
    btn1.configure(text='Comming Soon' , bg='blue', fg='yellow' , command=forgot)
def btn2():
    btn2.configure(text='Comming Soon' , bg='yellow', fg='blue' , command=delete)
def forgot():
    btn1.configure(text=' Forgot your account ?' , bg='blue', fg='yellow' , command=btn1)
def delete():
    btn2.configure(text='       Delete account       ' , bg='yellow', fg='blue' , command=btn2)
 
               
 # def homepage():
 #     win=tkinter.Tk()
 #     win.title('WELCOME!')
 #     win.geometry('700x200' )

 #     lbl=tkinter.Label(win , text='Hello! ' , fg='green')
 #     lbl.grid(column=6 , row=1)
 #     lbl=tkinter.Label(win , text='Sign In' , fg='black')
 #     lbl.grid(column=0 , row=1)
 #     lbl=tkinter.Label(win , text=' ')
 #     lbl.grid(column=0 , row=2)
 #     lbl=tkinter.Label(win , text='Sign Up ' , fg='black')
 #     lbl.grid(column=14 , row=1)
 #     lbl=tkinter.Label(win , text='                                ')
 #     lbl.grid(column=7 , row=0)

 #     lbl=tkinter.Label(win , text='   Username :' )
 #     lbl.grid(column=0 , row=3)
 #     userbox=tkinter.Entry(win , width=14 , bg='blue', fg='yellow')
 #     userbox.grid(column=1 , row=3 )

 #     lbl=tkinter.Label(win , text='   Password  :')
 #     lbl.grid(column=0 , row=4)
 #     passbox=tkinter.Entry(win , width=14 , bg='yellow', fg='blue' )
 #     passbox.grid(column=1 , row=4 )

 #     lbl=tkinter.Label(win , text=' ')
 #     lbl.grid(column=0 , row=5)
 #     lbl=tkinter.Label(win , text='                                ')
 #     lbl.grid(column=3 , row=0)

 #     btn=tkinter.Button(win , text='       Login         ' , bg='white', fg='black', command=GUI )
 #     btn.grid(column=1 , row=5)

 #     btn1=tkinter.Button( win , text=' Forgot your account ?' , bg='white', fg='black' )  #command=Forgot 
 #     btn1.grid(column=6 , row=4 )

 #     btn1=tkinter.Button( win , text='       Delete account       ' , bg='white', fg='black' ) #command=delete 
 #     btn1.grid(column=6 , row=5 )

 #     lbl24=tkinter.Label(win , text='    Username   :' , fg='black')
 #     lbl24.grid(column=14 , row=3)
 #     u2=tkinter.Entry(win , width=14 , bg='blue', fg='yellow')
 #     u2.grid(column=15 , row=3 )
 #     lbl28=tkinter.Label(win , text='*' , fg='blue')
 #     lbl28.grid(column=16 , row=3)
 #     lbl25=tkinter.Label(win , text='    Password    :' , fg='black')
 #     lbl25.grid(column=14 , row=4)
 #     p2=tkinter.Entry(win , width=14 , bg='yellow', fg='blue')
 #     p2.grid(column=15 , row=4 )
 #     lbl29=tkinter.Label(win , text='*' , fg='blue')
 #     lbl29.grid(column=16 , row=4)
 #     lbl26=tkinter.Label(win , text='    Phone NO. :' , fg='gray')
 #     lbl26.grid(column=14 , row=5)
 #     phonebox=tkinter.Entry(win , width=14 )
 #     phonebox.grid(column=15 , row=5 )
 #     lbl27=tkinter.Label(win , text='    email ADD. :' , fg='gray')
 #     lbl27.grid(column=14 , row=6)
 #     mailbox=tkinter.Entry(win , width=14 )
 #     mailbox.grid(column=15 , row=6 )
 #     btn=tkinter.Button(win , text='      Register       ' , bg='white', fg='black' , command=welcome) 
 #     btn.grid(column=15 , row=7)

 #     win.mainloop()
     
 #     u=userbox.get()
 #     p=passbox.get()
 #     with open('tkinter.json')as f:
 #         info=json.load(f)
 #         if(u in info and info[u]==p):
 #             win=tkinter.Tk()
 #             win.title('WELCOME!')
 #             win.geometry('250x100')
 #             lbl=tkinter.Label(win , text='      ')
 #             lbl.grid(column=0 , row=0)
 #             lbl=tkinter.Label(win , text='      ')
 #             lbl.grid(column=1 , row=0)
 #             lbl2=tkinter.Label(win ,text='      ')
 #             lbl2.grid(column=2 , row=1)
 #             lbl1=tkinter.Label(win , text='    W E L C O M E    ' , bg='blue', fg='yellow' )
 #             lbl1.grid(column=3 , row=1 )
 #             lbl1=tkinter.Label(win , text='         D E A R !          ' , bg='yellow', fg='blue' )
 #             lbl1.grid(column=3 , row=2 )
 #             win.mainloop()
         
 #         else:
 #             win=tkinter.Tk()
 #             win.title('New Tab')
 #             win.geometry('250x100')
 #             lbl2=tkinter.Label(win , text='Ohh! an error occured , please try again !')
 #             lbl2.grid(column=1 , row=1 )
 #             btn=tkinter.Button(win , text='    Home Page    ' , bg='white', fg='black' , command=welcome )
 #             btn.grid(column=1 , row=5)
 #             win.mainloop()


           
#main program    
   
win=tkinter.Tk()
win.title('WELCOME!')
win.geometry('700x200' )

lbl=tkinter.Label(win , text='Hello! ' , fg='green')
lbl.grid(column=6 , row=1)
lbl=tkinter.Label(win , text='Sign In' , fg='black')
lbl.grid(column=0 , row=1)
lbl=tkinter.Label(win , text=' ')
lbl.grid(column=0 , row=2)
lbl=tkinter.Label(win , text='Sign Up ' , fg='black')
lbl.grid(column=14 , row=1)
lbl=tkinter.Label(win , text='                                ')
lbl.grid(column=7 , row=0)

lbl=tkinter.Label(win , text='   Username :' )
lbl.grid(column=0 , row=3)
userbox=tkinter.Entry(win , width=14 , bg='blue', fg='yellow')
userbox.grid(column=1 , row=3 )

lbl=tkinter.Label(win , text='   Password  :')
lbl.grid(column=0 , row=4)
passbox=tkinter.Entry(win , width=14 , bg='yellow', fg='blue' )
passbox.grid(column=1 , row=4 )

lbl=tkinter.Label(win , text=' ')
lbl.grid(column=0 , row=5)
lbl=tkinter.Label(win , text='                                ')
lbl.grid(column=3 , row=0)

btn=tkinter.Button(win , text='       Login         ' , bg='white', fg='black', command=GUI )
btn.grid(column=1 , row=5)

btn1=tkinter.Button( win , text=' Forgot your account ?' , bg='white', fg='black' , command=btn1 ) 
btn1.grid(column=6 , row=4 )

btn2=tkinter.Button( win , text='       Delete account       ' , bg='white', fg='black' , command=btn2 )
btn2.grid(column=6 , row=5 )

lbl24=tkinter.Label(win , text='    Username   :' , fg='black')
lbl24.grid(column=14 , row=3)
u2=tkinter.Entry(win , width=14 , bg='blue', fg='yellow')
u2.grid(column=15 , row=3 )
lbl28=tkinter.Label(win , text='*' , fg='blue')
lbl28.grid(column=16 , row=3)
lbl25=tkinter.Label(win , text='    Password    :' , fg='black')
lbl25.grid(column=14 , row=4)
p2=tkinter.Entry(win , width=14 , bg='yellow', fg='blue')
p2.grid(column=15 , row=4 )
lbl29=tkinter.Label(win , text='*' , fg='blue')
lbl29.grid(column=16 , row=4)
lbl26=tkinter.Label(win , text='    Phone NO. :' , fg='gray')
lbl26.grid(column=14 , row=5)
phonebox=tkinter.Entry(win , width=14 )
phonebox.grid(column=15 , row=5 )
lbl27=tkinter.Label(win , text='    email ADD. :' , fg='gray')
lbl27.grid(column=14 , row=6)
mailbox=tkinter.Entry(win , width=14 )
mailbox.grid(column=15 , row=6 )
btn=tkinter.Button(win , text='      Register       ' , bg='white', fg='black' , command=signup) 
btn.grid(column=15 , row=7)


win.mainloop()