def isip(ip):
    a=ip.split(".")
    if len(a)==4:
        return True
    else: return False

def getip(text):
    b=text.split(" ")
    for obj in b:
        if isip(obj)==True:
            return obj
    return "0.0.0.0"
getip("blablabla bla bla target 195.255.365.1")