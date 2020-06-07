# -*- coding: utf-8 -*-

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

from typing import Text, NoReturn, Callable

class Mongo():

  def __init__(self, host: Text,
                user: Text,
                password: Text) -> NoReturn:
    self.host, self.user, self.password = host, user, password
    self.client = self.get_connection()

  def get_connection(self) -> MongoClient:
    try:
      conn = MongoClient(self.host, 27017, username=self.user, password=self.password)
      print("Mongo is connected!")
      return conn
    except ConnectionFailure as error:
      print(f"Could not connect to MongoDB: {error}")

  def show_status(self) -> NoReturn:
    print(self.client["admin"].command("serverStatus"))

if __name__ == "__main__":

  mongo = Mongo("mongodb", "user", "123456")
  mongo.show_status()
