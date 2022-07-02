class Person:

    def __init__(self,name1,surname,emailid1,year_of_birth):
        self.name = name1 
        self.surname1 = surname 
        self.emailid = emailid1
        self.year_of_birth = year_of_birth

    def age(self,current_year):
        return current_year - self.year_of_birth

anuj_variable = Person("anuj","bhandari","anuj@gmail.com",1994)

print(anuj_variable.name)
print(anuj_variable.surname1)
print(anuj_variable.emailid)
print(anuj_variable.name + anuj_variable.surname1)
print(type(anuj_variable)) 
print(anuj_variable.age(2022))