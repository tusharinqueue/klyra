import pickle
def create():
    l=[]
    xf=open("student.dat","wb")
    wish='y'
    while wish=='y':
        name=input("enter the name of the student")
        admo=int(input("enter the admisson no."))
        Class=int(input("enter the class of student"))
        l=[name,admo,Class]
        pickle.dump(l,xf)
        print(l)
        wish=input("if you want to enter more data please enter 'y' else press 'n'.")
    xf.close()
create()
