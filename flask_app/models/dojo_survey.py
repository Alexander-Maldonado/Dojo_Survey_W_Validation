from wsgiref import validate
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
class Ninja:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results =connectToMySQL("Dojo_Survey_Schema").query_db(query)
        ninjas = []
        for n in results:
            ninjas.append( cls(n) )
        return ninjas

    @classmethod
    def get_one(cls, data):
        query = "Select * from ninjas WHERE id =%(id)s;"
        results =connectToMySQL("Dojo_Survey_Schema").query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name) VALUES (%(first_name)s, %(last_name)s);"
        result = connectToMySQL("Dojo_Survey_Schema").query_db(query, data)
        return result

    @classmethod
    def update(cls, data):
        query = "UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, WHERE users.id = %(id)s;"
        return connectToMySQL("Dojo_Survey_Schema").query_db(query, data)


    @classmethod
    def delete(cls,data):
        query = "Delete from ninjas WHERE id = %(id)s;"
        return connectToMySQL("Dojo_Survey_Schema").query_db(query, data)

    @staticmethod
    def validate_ninja(ninja):
        is_valid = True
        if len(ninja["name"]) < 2:
            flash("Name must be at least 2 characters long.")
            is_valid = False
        if len(ninja["location"])<1:
            flash("Location must be selected.")
            is_valid = False
        if len(ninja["language"])<1:
            flash("Language must be selected.")
            is_valid = False
        if len(ninja["comment"])<10:
            flash("Comment of at least 10 characters must be left.")
            is_valid = False
        return is_valid