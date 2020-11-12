class Student:
    def __init__(self,name,laptop):
        self.name = name
        self.laptop = laptop
        self.height = 0
        self.sex = ''

    def __str__(self):
        return f"name:{self.name} laptop: {self.laptop} height: {self.height} sex: {self.sex}"

baiz = Student('baiz','razer')
baiz.height = 182
baiz.sex = 'male'
emir = Student('emir','lenovo')
emir.height = 180
emir.sex = 'male'
aijana = Student('aijana','hp')
aijana.height = 165
aijana.sex = 'female'
zarina = Student('zarina','acer')
zarina.height = 170
zarina.sex = 'female'
sultan = Student('sultan','macbook')
sultan.height = 175
sultan.sex = 'male'
nazira = Student('nazira','sony')
nazira.height = 169
nazira.sex = 'female'
print(baiz,emir,aijana,zarina,nazira,sultan)
