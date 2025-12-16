class BaseDAO:
    """Simple base DAO. Override methods to interact with storage."""

    def __init__(self):
        self._storage = {}

    def create(self, obj):
        """Create object and return stored id"""
        new_id = len(self._storage) + 1
        self._storage[new_id] = obj
        return new_id

    def read(self, obj_id):
        return self._storage.get(obj_id)

    def update(self, obj_id, obj):
        if obj_id in self._storage:
            self._storage[obj_id] = obj
            return True
        return False

    def delete(self, obj_id):
        return self._storage.pop(obj_id, None) is not None

    def list_all(self):
        return list(self._storage.values())
