from Const import *

Messages = ['0']*MsgBox_height

def Msg(message = None): # Send message to MessageBox
    global Messages
    if message != None:
        Messages = Messages[1:]
        Messages.append(message)
    return(Messages)
