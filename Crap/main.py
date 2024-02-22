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
""")
        if int(user) == 1:
             client_data = client_add().__dict__
             db.insert_client(client_data)
             print(f'\nyou have added {client_data["name"]}')
        elif int(user) == 2:
             print('you chose 2')
        elif int(user) == 3:
             print('you chose 3')
        elif int(user) == 4:
          print('you chose 4')
       # client_data = client_info().__dict__ # store client_info function return from user_input.py in client_data
       # db.insert_client(client_data) # pass client data as dictionary into insert_client method from database.py
       # user = input('would you like to add another client?') # ask user to add another

# exit contingency
       # if user.lower() == 'no': 
       #     print('we are done here')
       #     break

# user options menu will go here

if __name__ == "__main__":
    main()

