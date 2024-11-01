class student:
    grade=12
    name='Hope Chuga'

    def introduction(self):
        print('Hi, I am a student')

    def details(self):
        print('My name is',self.name)
        print('I am in grade',self.grade)

ob=student()
ob.introduction()
ob.details()