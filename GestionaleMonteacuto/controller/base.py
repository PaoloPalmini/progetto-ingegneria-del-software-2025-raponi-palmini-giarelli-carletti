class BaseController:
    """Simple base controller coordinating DAO and models."""

    def __init__(self, dao):
        self.dao = dao

    def create(self, model):
        return self.dao.create(model)

    def get(self, obj_id):
        return self.dao.read(obj_id)

    def update(self, obj_id, model):
        return self.dao.update(obj_id, model)

    def delete(self, obj_id):
        return self.dao.delete(obj_id)

    def list(self):
        return self.dao.list_all()
