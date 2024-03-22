import csv
import datetime
import matplotlib.pyplot as plt
def main_page():
    try:
        a=input("\nSelect one: sign_up, login, create_database ")
        if a=="sign_up":
            signup()
        elif a=="login":
            login()
        elif a=="create_database":
            print("\nThis will overwrite the current database, are you sure?\n")
            warning=input("Select yes or no: ")
            if warning=="yes":   
                new()
                print("\nSuccessfully created a new database")
                main_page()
            else:
                print("\nReturning to main page")
                main_page()
        else:
            print("\nPlease select an input only from the above options !")
            main_page()
    except Exception as e:
        print("Error in main_page:", e)
        
def new():
    try:
        savdat=open("user_data.csv","w")
        savdat.close()
        savdat2=open("expenses.csv","w")
        header=["USER-NAME","USER-BUDGET","FOOD-EXPENSES","TRANSPORT-EXPENSES","ENTERTAINMENT-EXPENSEES","HEALTHCARE-EXPENSES","MISCELLANEOUS-EXPENSES","DATE"]
        userdat=[header]
        writeup=csv.writer(savdat2)
        writeup.writerow(userdat)
        savdat2.close()
    except Exception as e:
        print("Error creating files:", e)

def signup():
    try:
        global acheck
        global a
        global b
        global c
        verifusernum=0
        print("\nDisclaimer -> please dont use the already taken usernames as it will lead to incorrect data or errors.\n")
        a=input("enter your username  ")
        b=input("enter your password  ")
        c=input("re-enter your password  ")
        savdat=open("user_data.csv","r")
        verifuserdoub=csv.reader(savdat)
        for x in verifuserdoub:
            if x[0]==a:
                verifusernum=verifusernum+1
                if verifusernum>=1:
                    print("sorry username already taken, please try some other username")
                    signup()
        pass_check()
    except Exception as e:
        print("Error during signup:", e)
        main_page()
def pass_check():
    try:
        global acheck
        global a
        global b
        global c
        if b!=c:
            while b!=c:
              print("the password re-entered does not match with original")
              b=input("enter your password  ")
              c=input("re-enter your password  ")
              if b==c:
                  break
        print("thank you for signing up with us",a)
        savdat=open("user_data.csv","a",newline="")
        userdat=[a,b]
        writeup=csv.writer(savdat)
        writeup.writerow(userdat)
        savdat.close()
        acheck=a
        start_app()
    except Exception as e:
        print("Error during password checking:", e)
        pass_check()

def login():
    try:
        usercount=0
        global acheck
        acheck=input("enter your username  ")
        bcheck=input("enter your password  ")
        savdat=open("user_data.csv","r")
        verif1=csv.reader(savdat)
        for line in verif1:
            if line[0]==acheck and line[1]==bcheck:
                usercount=usercount+1
        if usercount==1:
                print("welcome back",acheck)
                start_app()
        else:
            print("\nERROR ! username or password is incorrect , please retype the username and password or create a new account")
            login1=input("enter r if you want to re-login, enter p if you want to signup  ")
            if login1=="r":
                login()
            if login1=="p":
                signup()
            else:
                print("please enetr a valid input.")
                sign_up()
        savdat.close()
    except Exception as e:
        print("Error during login:", e)

def start_app():
    global acheck
    print("\nhello",acheck,"please select an option given below -")
    option()

def option():
    global acheck
    options=input("\n make_entry , display_report , compare_entries , exit -> ")
    if options=="make_entry":
                make_entry()
    elif options=="display_report":
               display_expenses()
    elif options=="compare_entries":
        compare_entries()
    elif options=="exit":
        print("\ngoodbye",acheck)
        main_page()
    else:
        print("please select a valid option")
        option()
        
def make_entry():
 try:
    global acheck
    entry=open("expenses.csv","a")
    budget=int(input("\nenter your total budget for this month-> "))
    food=int(input("\nenter your total expenditure on food for this month-> "))
    transport=int(input("\nenter your total expenditure on transport for this month-> "))
    entertainment=int(input("\nenter your total expenditure on entertainment for this month-> "))    
    healthcare=int(input("\nenter your total expenditure on healthcare for this month->  "))    
    miscellaneous=int(input("\nenter your total expenditure on miscellaneous things for this month-> "))
    date=datetime.datetime.now().date()
    list_obj=[acheck,budget,food,transport,entertainment,healthcare,miscellaneous,date]
    writeup=csv.writer(entry)
    writeup.writerow(list_obj)
    entry.close()
 except Exception as e:
     print("error making user entries :",e)
     make_entry()
 start_app()

def display_expenses():
    try:
        global acheck
        global selected_date
        print("\nMonthly expense report for:", acheck)
        dates = []  
        with open("expenses.csv", "r") as logs_file:
            reader = csv.reader(logs_file)
            next(reader)
            for row in reader:
                if row and row[0] == acheck:
                    print("Entry Date:", row[7])  
                    dates.append(row[7])
        if dates:
            selected_date = input("\nEnter the date (YYYY-MM-DD) of the entry you want to see the report for: ")
            if selected_date in dates:
                with open("expenses.csv", "r") as logs_file:
                    reader = csv.reader(logs_file)
                    next(reader)
                    for row in reader:
                        if row and row[0]==acheck and row[7]==selected_date:
                            print("\nUser:", row[0])
                            print("Budget:", row[1])
                            print("Food:", row[2])
                            print("Transport:", row[3])
                            print("Entertainment:", row[4])
                            print("Healthcare:", row[5])
                            print("Miscellaneous:", row[6])
                            print("Date of Entry:", row[7])
            else:
                print("Invalid date! Please select from the available dates.")
        else:
            print("No expenses found for", acheck)
    except Exception as e:
        print("Error displaying expenses:", e)
    display_report()


def display_report():
    try:
        global acheck
        global selected_date
        total_budget=0
        total_expenses=[0,0,0,0,0,0]
        with open("expenses.csv", "r") as logs_file:
            reader=csv.reader(logs_file)
            next(reader)  
            for row in reader:
                if len(row) >= 8 and row[0] == acheck and row[7]==selected_date:
                    total_budget += int(row[1])
                    for i in range(2, 7):
                        total_expenses[i - 2] += int(row[i])
        total_expenses.append(sum(total_expenses))
        projected_savings_month = total_budget - total_expenses[-1]
        projected_savings_year = projected_savings_month * 12
        print("\nProjected Savings for the Month:", projected_savings_month)
        print("Projected Savings for the Year:", projected_savings_year)
        labels = ['Food', 'Transport', 'Entertainment', 'Healthcare', 'Miscellaneous']
        sizes = total_expenses[:5]
        colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'orange']
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')
        plt.title('Expense Distribution')
        plt.show()
        if projected_savings_month < 100:
            print("\nYour expenses exceed your budget. You should consider reducing spending.")
        else:
            print("\nCongratulations! You are within your budget. Keep up the good work.")
    except Exception as e:
        print("Error displaying user report :", e)
    start_app()

def compare_entries():
    try:
        global acheck
        dates = set()
        entries = {}   
        with open("expenses.csv", "r") as logs_file:
            reader = csv.reader(logs_file)
            next(reader)
            for row in reader:
                if row and row[0] == acheck:
                    date = row[7]
                    dates.add(date)
                    if date in entries:
                        entries[date].append(row)
                    else:
                        entries[date]=[row]
        if len(dates) < 2:
            print("\nNot enough entries for comparison.")
            return
        dates=sorted(dates)
        categories=["Food","Transport","Entertainment","Healthcare","Miscellaneous"]
        data={category: [] for category in categories}
        for date in dates:
            for category in categories:
                total=sum(int(row[categories.index(category) + 2]) for row in entries[date])
                data[category].append(total)
        plt.figure(figsize=(10, 6))
        for category in categories:
            plt.plot(dates, data[category], label=category)
        plt.title("Comparison of Expenses Over Different Dates")
        plt.xlabel("Date")
        plt.ylabel("Total Expense")
        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print("Error comparing entries:", e)
    start_app()
    
main_page()
