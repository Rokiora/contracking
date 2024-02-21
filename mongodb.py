import pymongo

# set up connection
myclient = pymongo.MongoClient("mongodb://localhost:27017")

# creating databse object
mydb = myclient['contract_fulfilment']

# instantiating collection (will not get created until content is added)
mycol = mydb['clients']

class Client:
    def __init__(self, name, start, end, codes, vine, clinint, report_due, submitted):
             self.name = name 
             self.start = start
             self.end = end
             self.codes = codes
             self.vine = vine
             self.clinint = clinint
             self.report_due = report_due
             self.submitted = submitted

def user_input():
    uname = input('Enter client pseudonym')
    ustart = input('Enter contract start date')
    uend = input('Enter contract end date')
    uvine = input('Has the vineland been conducted?')
    uclinint = input('Has the clinical interview been conducted?')
    ureport_due = 'empty for now'
    usubmitted = input('Have you submitted this report to the regional clinical director?')

    ucodes = []

    user = 'x'

    while user != 'no':
         code = input('enter code: ')
         total = input('total hours: ')
         used = input('enter used hours: ')
         user = input('would you like to add another code?')
         ucodes.append({'code': code, 'total': total, 'used': used})

    return Client(name=uname, start=ustart, end=uend, codes=ucodes, vine=uvine, report_due=ureport_due, clinint=uclinint, submitted=usubmitted)

def client_add():
      user = 'x'
      while user != 'no':
            client = user_input()
            mycol.insert_one(client.__dict__)
            user = input('would you like to add another?: ')


# add my clients to 



# snippet for checking whats in my collection            
#for x in mycol.find():
#      print(x)


    
