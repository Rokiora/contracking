from database import Database
from user_input import client_info


def main():
# this block provides db connection information
    db_url = "mongodb://localhost:27017"
    db_name = "contract_fulfilment"
    collection_name = "clients"

# set db variable so Databse methods know where to execute
    db = Database(db_url,db_name,collection_name)

# main loop
    while True: # may need to change this loop, perhaps replaced with a function? for simplicity? function should handl options (add client, update client, etc.)
        client_data = client_info().__dict__ # store client_info function return from user_input.py in client_data
        db.insert_client(client_data) # pass client data as dictionary into insert_client method from database.py
        user = input('would you like to add another client?') # ask user to add another

# exit contingency
        if user.lower() == 'no': 
            print('we are done here')
            break

if __name__ == "__main__":
    main()

