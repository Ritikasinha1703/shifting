original=input("enter a word").upper()
dict= {"A":"C","B":"D","C":"E","D":"F","E":"G","F":"H","G":"I","H":"J","I":"K",
        "J":"L","K":"M","L":"N","M":"O","N":"P","O":"Q","P":"R","Q":"S","R":"T",
        "S":"U","T":"V","U":"W","V":"X","W":"Y","X":"Z","Y":"A","Z":"B"}
try:
    o=list(original)
    print("the obtained string is")
    for i in o:
        print(dict[i],end="").lower()
except:
    print("enter a valid string")
