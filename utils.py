from database import database

def insertData(to: str, newData) -> None:
    """
    Insert New Data To Particular Key

    :param to: To where the data will be inserted
    :param newData: Data you want to insert
    """ 

    if not (database.get(to) is None):
        if isinstance(database[to], list):
            database[to].append(newData)    
    else:
        database[to] = newData