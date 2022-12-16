class employee:
    company="Youtube"
    def getsalary(self):
        print(f"salary is: {self.salary}")
    @staticmethod     #Either pass self to function or declare it to staticMethod...
    def geet():
        print("Hello everyone")
ashu=employee()
arun=employee()
arun.salary=200   #instance variable
ashu.salary=400
arun.getsalary()    #equvivalent to ->>>>>>>           *******employee.getsalary(arun)*********
arun.geet()
# print(arun.company,arun.salary)
# print(ashu.company,ashu.salary)