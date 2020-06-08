# -*- coding: utf-8 -*-

try:
  from urllib.parse import quote_plus
except ImportError:
  from urllib import quote_plus

from bson import ObjectId
from datetime import datetime
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError

from typing import Text, NoReturn, Callable

class Mongo():

  def __init__(self, host: Text,
                user: Text,
                password: Text,
                port=27017, *args, **kwargs) -> NoReturn:
    self.uri = f"mongodb://{quote_plus(user)}:{quote_plus(password)}@{host}:{port}"
    self.client = self.get_connection()
    self.db = self.client["tweets"]
    self.logger = kwargs["logger"]

  def get_connection(self) -> MongoClient:
    try:
      conn = MongoClient(self.uri, serverSelectionTimeoutMS=1)
      conn.server_info()
      try:
        conn.admin.command("ismaster")
      except ConnectionFailure:
        self.logger.error(f"Could not connect to MongoDB: {error}")
      finally:
        try:
          conn["admin"].command("serverStatus")
        except Exception as error:
          self.logger.error(f"General Exception Mongo - {error}")
        else:
          self.logger.info("You are connected!")
        return conn
    except ServerSelectionTimeoutError  as error:
      self.logger.error(f"Server Timeout Error - {error}")

  def insert(self, element, collection_name):
    element["created"] = datetime.now()
    element["updated"] = datetime.now()
    inserted = self.db[collection_name].insert_one(element)
    return str(inserted.inserted_id)

  def delete(self, id, collection_name):
    deleted = self.db[collection_name].delete_one(
      {"_id":
        ObjectId(id)
      }
    )
    return bool(deleted.deleted_count)

  def find(self, criteria,
            collection_name,
            projection=None,
            sort=None,
            limit=0, cursor=False):
    if "_id" in criteria:
      criteria["_id"] = ObjectId(criteria["_id"])
    found = self.db[collection_name].find(
      filter=criteria,
      projection=projection,
      limit=limit,
      sort=sort
    )
    if cursor:
      return found
    found = list(found)
    for i in range(len(found)):
      if "_id" in found[i]:
        found[i]["_id"] = str(found[i]["_id"])
    return found

  def find_by_id(self, id, collection_name):
    found = self.db[collection_name].find_one(
      {"_id":
        ObjectId(id)
      }
    )
    if found is None:
      return not found
    if "_id" in found:
      found["_id"] = str(found["_id"])
    return found

  def close_connection(self) -> NoReturn:
    self.logger.info("Connection getting closed")
    self.client.close()

  def list_databases(self) -> NoReturn:
    for index, value in enumerate(self.client.list_database_names(), start=1):
      self.logger.info(f"Database {index} - {value}")

  def show_status(self) -> NoReturn:
    self.logger.info(self.client["admin"].command("serverStatus"))
