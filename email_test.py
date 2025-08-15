import gmail
#replace with your email_id & app_passs
email_id="" #your gmail id
app_pass="" #app pass
def send_openacn_ack(uemail,uname,uacn,upass):
    con=gmail.GMail(email_id,app_pass)
    sub="Congratulation😊,Account opened sucessfully"
    utext="""Hello,{uname}
    Welcome to ABC Bank
    Your Acc No is {uacm}
    Your Pass is {upass}
    Kindly change your password when you login first

    Thanks 
    ABC Bank
    Noida
    """
    msg=gmail.Message(to=uemail,subject=sub,text=utext)
    con.send(msg)

def send_otp(uemail,otp,amt):
    con=gmail.GMail(email_id,app_pass)
    sub="OTP for Fund Transfer"
    utext=f"""Your otp is {otp} to transfer amount{amt}

    Kindly use this OTP to complete transfer
    Please do not share OTP to anyone else

    Thanks 
    ABC Bank
    Noida
    """
    msg=gmail.Message(to=uemail,subject=sub,text=utext)
    con.send(msg)

def send_otp_4_pass(uemail,otp):
    con=gmail.GMail(email_id,app_pass)
    sub="OTP for password recovery"
    utext=f"""Your otp is {otp} to recover password

    Please do not share OTP to anyone else

    Thanks 
    ABC Bank
    Noida
    """
    msg=gmail.Message(to=uemail,subject=sub,text=utext)
    con.send(msg)
    

