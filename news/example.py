MyrecordsList=[]
class Myrecords:
    def __init__(self):
        self.title ='No Title'
        self.desc ='No Desc'
    def save(self):
        MyrecordsList.append(self)

m =Myrecords()
m.title =input("enter title")
m.desc=input("ener desc")
m.save()
print(m.title)
print(m.desc)

print(MyrecordsList)
