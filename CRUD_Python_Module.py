# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, USER, PASS, HOST, PORT, DB, COL): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        if data is not None: 
            insert = self.database.animals.insert_one(data)  # data should be dictionary
            if insert != 0:
                return True
            else:
                return False
        else: 
            raise Exception("Nothing to save, because data parameter is empty") 

    # Create method to implement the R in CRUD.
    def read(self, data):
        if data is not None:
            cursor = self.collection.find(data)
            return list(cursor) 
        else:
            raise Exception("Nothing to read, because data parameter is empty")
            
    # Create method to implement the U in CRUD     
    def update(self, query, new_data):
        if query is not None and new_data is not None:
            result = self.collection.update_many(query, {"$set": new_data})
            return result.modified_count
        else:
            raise Exception("Update failed: Query or data parameter is empty")

    # Create method to implement the D in CRUD
    def delete(self, query):
        if query is not None:
            result = self.collection.delete_many(query)
            return result.deleted_count
        else:
            raise Exception("Delete failed: Query parameter is empty")