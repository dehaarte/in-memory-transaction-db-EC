
class InMemoryDB:
    def __init__(self):
        self._main_state = {}
        self._transaction_changes = {}
        self._transaction_in_progress = False
    
    def get(self, key):
        return self._main_state.get(key)
    
    def put(self, key, val):
        if not self._transaction_in_progress:
            raise RuntimeError("put() called when a transaction is not in progress")
        self._transaction_changes[key] = val
    
    def begin_transaction(self):
        if self._transaction_in_progress:
            raise RuntimeError("A transaction is already in progress")
        self._transaction_in_progress = True
        self._transaction_changes.clear()
    
    def commit(self):
        if not self._transaction_in_progress:
            raise RuntimeError("commit() called when a transaction is not in progress")
        self._main_state.update(self._transaction_changes)
        self._transaction_changes.clear()
        self._transaction_in_progress = False
    
    def rollback(self):
        if not self._transaction_in_progress:
            raise RuntimeError("rollback() called when a transaction is not in progress")
        self._transaction_changes.clear()
        self._transaction_in_progress = False