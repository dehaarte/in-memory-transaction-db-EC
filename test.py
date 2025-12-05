from in_memory_db import InMemoryDB

def run_tests():
    inmemoryDB = InMemoryDB()
    
    print('get("A"):', inmemoryDB.get("A"))
    try:
        inmemoryDB.put("A", 5)
    except RuntimeError as e:
        print('put("A", 5) ERROR:', e)
        
    print("begin_transaction()")
    inmemoryDB.begin_transaction()
    
    print('put("A", 5)')
    inmemoryDB.put("A", 5)
    print('get("A"):', inmemoryDB.get("A"))
    
    print('put("A", 6)')
    inmemoryDB.put("A", 6)
    
    print("commit()")
    inmemoryDB.commit()
    
    print('get("A"):', inmemoryDB.get("A"))
    
    try:
        inmemoryDB.commit()
    except RuntimeError as e:
        print("commit() ERROR:", e)
        
    try:
        inmemoryDB.rollback()
    except RuntimeError as e:
        print("rollback() ERROR:", e)
        
    print('get("B"):', inmemoryDB.get("B"))
    
    print("begin_transaction()")
    inmemoryDB.begin_transaction()
    
    print('put("B", 10)')
    inmemoryDB.put("B", 10)
    
    print("rollback()")
    inmemoryDB.rollback()
    print('get("B"):', inmemoryDB.get("B"))
    
if __name__ == "__main__":
    run_tests()