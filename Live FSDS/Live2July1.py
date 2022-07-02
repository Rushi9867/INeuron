class Person:
    def age(self,current_year , year_of_birth):
        return current_year - year_of_birth

    def email_id_input(self,email_id):
        print("Take and Mail id from a person and print it ",email_id)

    def ask_name(self):
        name = input("Tell me your name ")
        return name 

    def ask_dob(self):
        dob = input("Tell me your date of birth ")
        return dob 

sudh = Person()
anuj = Person()
krish = Person()

sudh.email_id_input("sudhanshu@ineron.ai")
print(sudh.ask_name())

print(krish.ask_dob())