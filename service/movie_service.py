class MovieService:
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
        model_item.title = data.get('title')
        model_item.description = data.get('description')
        model_item.trailer = data.get('trailer')
        model_item.rating = data.get('rating')
        model_item.year = data.get('year')
        model_item.genre_id = data.get('genre_id')
        model_item.director_id = data.get('director_id')
        self.dao_model.update(model_item)
        return model_item

    def update_part(self, iid, data):
        model_item = self.get_one(iid)
        if data.get('title'):
            model_item.title = data.get('title')
        if data.get('description'):
            model_item.description = data.get('description')
        if data.get('trailer'):
            model_item.trailer = data.get('trailer')
        if data.get('rating'):
            model_item.rating = data.get('rating')
        if data.get('year'):
            model_item.year = data.get('year')
        if data.get('genre_id'):
            model_item.genre_id = data.get('genre_id')
        if data.get('director_id'):
            model_item.director_id = data.get('director_id')
        self.dao_model.update(model_item)
        return model_item

    def create(self, data):
        model_item = self.dao_model.create(data)
        return model_item

    def delete(self, iid):
        self.dao_model.delete(iid)
        return "", 204
