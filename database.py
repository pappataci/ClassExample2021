def create_database_entry(name, id_no, age):
    new_patient = [name , id_no, age, []  ]
    return new_patient
    
def print_directory(db):
    for patient in db:
        print("Name: {}, id: {}, age: {}".format(patient[0] , patient[1], patient[2]) )
  
def find_patient(id_no, db):
    for item in db:
        
        if item[1] == id_no:
            return  item[0]
            
            
    return "Patient not found"
    

def add_test_result(id_no, db, test_name, test_result):
    for patient in db:
        if patient[1] == id_no:
            patient[3].append( (test_name, test_result) )
     
     
def main():
    db = list()
    db.append(create_database_entry("ann ables", 1, 30))
    db.append(create_database_entry("bob boyles", 2, 31))
    db.append(create_database_entry("chris chou", 3, 32))
    db.append(create_database_entry("david dinkins", 4, 33))
    
    add_test_result(3, db , "HDL", 65)
    add_test_result(3, db, "LDL" , 80 )
    
    # print_directory(db)

    
if __name__ ==  '__main__':
    main()