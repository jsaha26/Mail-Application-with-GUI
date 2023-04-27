from tkinter import *
from tkinter import filedialog
import smtplib
from email.message import EmailMessage

#Global variables
attachments =[]

#Main Screen
root = Tk()
root.title('Mail Application')

#Functions
def attachFile():
    filename = filedialog.askopenfilename(initialdir='c:/',)
    attachments.append(filename)
    notif.config(fg='green', text = 'Attached ' + str(len(attachments)) + ' files')
   

def send():
    try:
        msg = EmailMessage()
        username = temp_username.get()
        password = temp_password.get()
        to = temp_receiver.get()
        subject = temp_subject.get()
        body = temp_body.get()
        msg['subject'] = subject
        msg['from'] = username
        msg['to'] = to
        msg.set_content(body)

        for filename in attachments:
            filename = attachments[0]
            filetype = filename.split('.')
            filetype = filetype[1]
        
            if filetype == 'jpg' or filetype == 'png' or filename == 'jpeg':
                import imghdr
                with open(filename, 'rb') as f:
                    file_data = f.read()
                    image_type = imghdr.what(filename)
                msg.add_attachment(file_data, maintype = 'image', subtype = image_type, filename=f.name)
            else:
                with open(filename, 'rb') as f:
                    file_data = f.read()
                msg.add_attachment(file_data, maintype = 'application', subtype = 'octet-stream', filename=f.name)



        if username=='' or password=='' or to=='' or subject=='' or body=='':
            notif.config(text = 'All fields are required', fg = 'red')
            return
        else:
            server = smtplib.SMTP('smtp.zohomail.in',587)
            server.starttls()
            server.login(username, password)
            server.send_message(msg)
            notif.config(text='Email has been sent', fg='green')
    except:
        notif.config(text = 'An error occured while sending email', fg = 'red')
    print('Sent')

def reset():
    usernameEntry.delete(0,'end')
    passwordEntry.delete(0,'end')
    receiverEntry.delete(0,'end')
    subjectEntry.delete(0,'end')
    bodyEntry.delete(0,'end')

#Graphics
titleLabel = Label(root, text="Custom Email Application", font=('Roboto', 15))
titleLabel.grid(row=0, column=1, padx=10, pady=10)

Label(root, text='Send an email', font=('Roboto', 11)).grid(row=1, column=0, sticky=W, padx=10)

Label(root, text='Email', font=('Roboto', 11)).grid(row=2, column=0, sticky=W, padx=10)
Label(root, text='Password', font=('Roboto', 11)).grid(row=3, column=0, sticky=W, padx=10)
Label(root, text='To', font=('Roboto', 11)).grid(row=4, column=0, sticky=W, padx=10)
Label(root, text='Subject', font=('Roboto', 11)).grid(row=5, column=0, sticky=W, padx=10)
Label(root, text='Body', font=('Roboto', 11)).grid(row=6, column=0, sticky=W, padx=10)

notif = Label(root, text='', font=('Roboto', 11))
notif.grid(row=8, column=1, padx=10, pady=10, sticky=W)


#Storage
temp_username = StringVar()
temp_password = StringVar()
temp_receiver = StringVar()
temp_subject = StringVar()
temp_body = StringVar()

#Entries
usernameEntry = Entry(root, textvariable=temp_username, width=50)
usernameEntry.grid(row=2, column=1, padx=10, pady=10)
passwordEntry = Entry(root, show='*', textvariable=temp_password, width=50)
passwordEntry.grid(row=3, column=1, padx=10, pady=10)
receiverEntry = Entry(root, textvariable=temp_receiver, width=50)
receiverEntry.grid(row=4, column=1, padx=10, pady=10)
subjectEntry = Entry(root, textvariable=temp_subject, width=50)
subjectEntry.grid(row=5, column=1, padx=10, pady=10)
bodyEntry = Entry(root, textvariable=temp_body, width=50)
bodyEntry.grid(row=6, column=1, padx=10, pady=10)


#Buttons
Button(root, text="Send", command=send, font=('Roboto', 11)).grid(row=7, column=0, padx=10, pady=10)
Button(root, text="Reset", command=reset, font=('Roboto', 11)).grid(row=7, column=1, padx=10, pady=10, sticky=E)
Button(root, text="Attachments", command=attachFile, font=('Roboto', 11)).grid(row=7, column=1, padx=100, pady=10, sticky=E)


root.mainloop()