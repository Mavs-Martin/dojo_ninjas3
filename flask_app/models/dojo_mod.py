from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja_mod

DATBASE = "dojos_and_ninja_schema"


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.create_at = data['create_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = """SELECT * FROM dojos;"""
        results = connectToMySQL(DATBASE).query_db(query)
        dojo_list = []

        for result in results:
            dojo_list.append(cls(result))
        return dojo_list

    @classmethod
    def create_location(cls, data):
        query = """INSERT INTO dojos (name) VALUE (%(name)s);"""
        result = connectToMySQL('dojos_and_ninja_schema').query_db(query, data)
        return result

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id =%(id)s;"
        results = connectToMySQL(
            'dojos_and_ninja_schema').query_db(query, data)
        # print(results)
        dojo = cls(results[0])
        for row in results:
            one_ninja = {
                "id": row["ninjas.id"],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['created_at'],
                'updated_at': row['ninjas.updated_at']
            }
            dojo.ninjas.append(ninja_mod.Ninja(one_ninja))
        return dojo
