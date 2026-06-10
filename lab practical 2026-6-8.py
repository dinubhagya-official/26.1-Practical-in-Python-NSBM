age = int(input(" Enter Your Age : "))
citi = input(" Are you a citizen (Yes/No) : ")
if age >= 18:
    if citi == "Yes"or"yes":
        print("Eligible")
    else:
        print("You Are Not Eligible")
else:
     print("Your age is not match")

##############################################

balance = 20000
pin = str(input(" Enter your pin : "))
if pin=="1234":
    cash = float(input(" Enter your cash withdrawal : ")) 
    if cash<=balance:
        print(" here your cash ")
    else:
        print(" this cash over to 20000 ")
else:
    print(" Your pin number is incorrect ")

###################################################

mark = float(input(" Enter Student Marks : "))
if mark >=75:
    income = float(input(" Enter Student family Income : "))

    if income <50000:
        print(" Scholorship eligiable ")
    else:
        print(" Scholorship not eligiable ")
else:
    print(" your mark not eligiable ")

#######################################################

student = input("Are you registered (yes/no) : ")
if student == "Yes" or student == "yes":
    fee = input("Must you pay the exam fee (yes/no) : ")
    if fee == "Yes" or fee == "yes":
        print("Your exam seat is ready!")
    else:
        print("Please pay your exam fee first.")
else:
    print("Please register before the exam.")

#################################################################

    log = input(" are you log in (yes/no) : ")

if log=="Yes"or log=="yes":
    cart=float(input(" Enter the cart value : "))
    if cart>=1000:
        payment=input(" payment successful (yes/no) : ")
        if payment=="Yes"or payment=="yes":
            print(" order confirmed ")
        else:
            print(" payment unsuccessful ")
    else:
        print(" cart value not eligiable ")
else:
    print(" plese log in come back ")
     
