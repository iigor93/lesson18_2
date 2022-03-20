class GenreService:
    def __init__(self, dao_model):
        self.dao_model = dao_model

    def get_all(self):
        all_items = self.dao_model.get_all()
        return all_items

    def get_one(self, iid):
        one_item = self.dao_model.get_one(iid)
        return one_item

    def update_all(self, iid, data):
        model_item = self.get_one(iid)
        model_item.name = data.get('name')
        self.dao_model.update(model_item)
        return model_item

    def update_part(self, iid, data):
        model_item = self.get_one(iid)
        if data.get('name'):
            model_item.name = data.get('name')
        self.dao_model.update(model_item)
        return model_item

    def create(self, data):
        model_item = self.dao_model.create(data)
        return model_item

    def delete(self, iid):
        self.dao_model.delete(iid)
        return "", 204
