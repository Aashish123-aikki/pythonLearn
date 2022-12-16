class employee:
    company="Youtube"
    a=0
    @staticmethod
    def __init__() -> None:
        employee.a=employee.a+1
        print(f"Employee Created! with Id EMPhr10{employee.a} ")
    def getsalary(self):
        print(f"salary is: {self.salary}")
    @staticmethod     #Either pass self to function or declare it to staticMethod...
    def geet():
        print("Hello everyone")

harry=employee()
arun=employee()