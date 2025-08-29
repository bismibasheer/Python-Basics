class student:
    institude="oneteam"

    def get_details(self,n,a):
        self.name=n
        self.age=a

    def display(self):
        print(f"your name is {self.name} and age {self.age}")  
st1=student()
st2=student()

st1.get_details("Bismi",23)
st2.get_details("Ano",24)
print(st1.name)
print(st2.name)
st2.display()