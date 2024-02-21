from client import Client
import datetime
from datetime import timedelta


# user options menu will go here
def main_menu():
     print('what would you like to do?')
     user = input(
          """
1. add a new client
2. update client data
3. check upcoming reports
4. delete client
""")
     if int(user) == 1:
          client_add()
     elif int(user) == 2:
          print('you chose 2')
     elif int(user) == 3:
          print('you chose 3')
     elif int(user) == 4:
          print('you chose 4')
          



# client addition module
#strptime parses string into datetime object
#strftime converts object to desired string format
def client_add():
    uname = input('Enter client pseudonym: ')
    ustart = datetime.datetime.strptime(input('Enter contract start date (dd mm yy): '), "%d %m %y").date().strftime("%d-%m-%y")
    uend = datetime.datetime.strptime(input('Enter contract end date (dd mm yy): '), "%d %m %y").date().strftime("%d-%m-%y")
    uvine = input('Has the vineland been conducted?: ')
    uclinint = input('Has the clinical interview been conducted?: ')
    ureport_due = uend - timedelta(weeks=6)
    usubmitted = input('Have you submitted this report to the regional clinical director?')

    ucodes = []


    while True:
         code = input('enter code: ')
         total = input('total hours: ')
         used = input('enter used hours: ')
         ucodes.append({'code': code, 'total': total, 'used': used})
         user = input('would you like to add another code?')
         if user.lower() == 'no':
              break

    return Client(name=uname, start=ustart, end=uend, codes=ucodes, vine=uvine, report_due=ureport_due, clinint=uclinint, submitted=usubmitted)


# client update will go here

# check upcoming reports


# delete client