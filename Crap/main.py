from database import Database
from user_input import client_add



def main():
# this block provides db connection information
    db_url = "mongodb://localhost:27017"
    db_name = "contract_fulfilment"
    collection_name = "clients"

# set db variable so Databse methods know where to execute
    db = Database(db_url,db_name,collection_name)

# main loop
    while True: # may need to change this loop, perhaps replaced with a function? for simplicity? function should handl options (add client, update client, etc.)
        user = input(
          """
what would you like to do?
1. add a new client
2. update client data
3. check upcoming reports
4. delete client
5. exit
""")
        if int(user) == 1:
             client_data = client_add().__dict__ # client_data = client_info().__dict__ # store client_info function return from user_input.py in client_data
             db.insert_client(client_data) # db.insert_client(client_data) # pass client data as dictionary into insert_client method from database.py
             print(f'\nyou have added {client_data["name"]}') # indicate which client has been added
        elif int(user) == 2:
             print('you chose 2')
        elif int(user) == 3:
             upcoming = db.collection.find().sort("report_due", 1) # sort clients by report due date starting from the most recent
             if db.collection.count_documents({}) >= 3:
                 for i in range(3):
                     client = upcoming[i]
                     print(f'{client["name"]} is due {client["report_due"]}') # print the list of clients 
             else:
                for client in upcoming:
                 print(f'{client["name"]} is due {client["report_due"]}') # print the list of clients 
# ^ maybe limit to show only 3? instead of the whole
        elif int(user) == 4:
          print('you chose 4')

# exit contingency
        elif int(user) == 5: 
            print('we are done here')
            break
    
# user options menu will go here

if __name__ == "__main__":
    main()

