#Lab.4 institutional gmail generator
#student willl creat a function that automatically generates an institutional email address from a person's first name and lastname

#variable declarations
name="Sebastian"
lastname="Rios"

def generate_email(name, lastname):
    email= f"{name.lower()}.{lastname.lower()}@utd.edu.mx"
    return email 

#Main program
generated_email=generate_email(name,lastname)

print("Your Institutional email is:", generated_email)
r="si"
while r=="yes":
    name=input("Ingresa tu nombre: ")
    lastname=input("Ingresa tu apellido: ")

    def generate_email(name, lastname):
        email= f"{name.lower()}.{lastname.lower()}@utd.edu.mx"
        return email 

    #Main program
    generated_email=generate_email(name,lastname)

    print("Your Institutional email is:", generated_email)
    r=input("Do you want to introduce another? yes/no: ").lower()
    