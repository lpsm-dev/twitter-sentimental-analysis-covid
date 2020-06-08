from tools.validate import Validator
from database.mongo import Mongo

class Todo(object):
  def __init__(self):
    self.validator = Validator()
    self.db = Database()
    self.collection_name = "tweets"

    self.fields = {
      "title": "string",
      "body": "string",
      "created": "datetime",
      "updated": "datetime",
    }

    self.create_required_fields = ["title", "body"]
    self.create_optional_fields = []
    self.update_required_fields = ["title", "body"]
    self.update_optional_fields = []

  def create(self, tweet):
    self.validator.validate(tweet, self.fields, self.create_required_fields, self.create_optional_fields)
    res = self.db.insert(tweet, self.collection_name)
    return "Inserted Id " + res

  def find(self, tweet):
    return self.db.find(tweet, self.collection_name)

  def find_by_id(self, id):
    return self.db.find_by_id(id, self.collection_name)

  def update(self, id, tweet):
    self.validator.validate(tweet, self.fields, self.update_required_fields, self.update_optional_fields)
    return self.db.update(id, tweet, self.collection_name)

  def delete(self, id):
    return self.db.delete(id, self.collection_name)
