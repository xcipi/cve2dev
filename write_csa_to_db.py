from pymongo import MongoClient
import datetime

# creating connectioons for communicating with Mongo DB
client = MongoClient('localhost:27017')
db = client.CSAs

def main():
    while(1):
        # chossing option to do CRUD operations
        # if you want add main() at the end
        
        selection = input('\nSelect 1 to insert, 2 to update, 3 to read, 4 to delete\n')
    
        if selection == '1':
            insert()
        elif selection == '2':
            update()
        elif selection == '3':
            read()
        elif selection == '4':
            print ('delete')
            delete()
        else:
            print ('\n INVALID SELECTION \n')


# Function to insert data into mongo db
def insert_csa():
    try:
        slaId = input('Enter SLA ID: ')
        slaCustomer = input('Enter SLA customer: ')
        slaType = input('Enter SLA type (5x8xNBD,7x24,...): ')
        
        db.slas.insert_one(
            {
                "slaId": slaId,
                "slaCustomer": slaCustomer,
                "slaType": slaType,
            })
        print ('\nInserted data successfully\n')
        
    except:
        print ('ERROR')

# Function to update record to mongo db
def update_csa():
    try:
        criteria = input('\nEnter SLA ID to update: \n')
        customer = input('\nEnter new SLA customer: \n')
        type = input('\nEnter new SLA type: \n')

        db.slas.update_one(
            {"slaId": criteria},
            {
                "$set": {
                    "slaCustomer":customer,
                    "slaType":type,
                }
            }
        )
        print ("\nRecords updated successfully\n")
        
    except:
        print ('ERROR')

# function to read records from mongo db    
def read_csa():
    try:
        slaCol = db.slas.find()
        print ('\n All data from SLA Database \n', db)
        for sla in slaCol:
            print (sla)
    except:
        print ('ERROR')



def delete_csa():
    print('delete')

