from dao.models.movie_model import Movie as ModelClass


class MoviesDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        all_item = self.session.query(ModelClass).all()
        return all_item

    def get_all_filter(self, req):
        all_item = ModelClass.query.filter_by(**req).all()
        return all_item

    def get_one(self, iid):
        one_item = ModelClass.query.get(iid)
        return one_item

    def create(self, data):
        model_item = ModelClass(**data)
        self.session.add(model_item)
        self.session.commit()
        return model_item

    def update(self, model_item):
        self.session.add(model_item)
        self.session.commit()

    def delete(self, iid):
        model_item = self.get_one(iid)
        self.session.delete(model_item)
        self.session.commit()
