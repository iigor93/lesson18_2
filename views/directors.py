from flask_restx import Namespace, Resource
from flask import jsonify, request
from dao.models.director_model import DirectorSchema as ModelSchema
from implemented import director_service_obj as service_obj


directors_ns = Namespace('directors')


@directors_ns.route('/')
class Items_all(Resource):
    def get(self):
        all_items = service_obj.get_all()
        all_item_schema = ModelSchema(many=True)
        return jsonify(all_item_schema.dump(all_items))

    def post(self):
        data = request.json
        service_obj.create(data)
        return "", 201


@directors_ns.route('/<int:iid>')
class Item_one(Resource):
    def get(self, iid):
        one_item = service_obj.get_one(iid)
        if one_item:
            item_schema = ModelSchema()
            data_to_return = item_schema.dump(one_item)
            return jsonify(data_to_return)
        return "", 404

    def put(self, iid):
        data = request.json
        service_obj.update_all(iid, data)
        return "", 201

    def patch(self, iid):
        data = request.json
        service_obj.update_part(iid, data)
        return "", 201

    def delete(self, iid):
        service_obj.delete(iid)
        return "", 204

