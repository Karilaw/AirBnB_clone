#!/usr/bin/python3
"""a class FileStorage that serializes instances to a
JSON file and deserializes JSON file to instances
"""


import json


class FileStorage:
    """A class that serializes instances to a JSON
    file and deserializes JSON file to instances.

    Attributes:
        __file_path (str): The path to the JSON file.
        __objects (dict): A dictionary that stores
        all objects by <class name>.id.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects.

        Returns:
            dict: The dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id.

        Args:
            obj: The object to be added to the __objects dictionary.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        data = {}
        for key, value in FileStorage.__objects.items():
            data[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(data, f)

    def reload(self):
        """Deserializes the JSON file to __objects.

        Only if the JSON file (__file_path) exists; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised.
        """
        try:
            with open(FileStorage.__file_path, "r") as f:
                data = json.load(f)
            for key, value in data.items():
                class_name = value["__class__"]
                if class_name == "BaseModel":
                    from models.base_model import BaseModel
                    FileStorage.__objects[key] = BaseModel(**value)
                elif class_name == "User":
                    from models.user import User
                    FileStorage.__objects[key] = User(**value)
                elif class_name == "Place":
                    from models.place import Place
                    FileStorage.__objects[key] = Place(**value)
                elif class_name == "State":
                    from models.state import State
                    FileStorage.__objects[key] = State(**value)
                elif class_name == "City":
                    from models.city import City
                    FileStorage.__objects[key] = City(**value)
                elif class_name == "Amenity":
                    from models.amenity import Amenity
                    FileStorage.__objects[key] = Amenity(**value)
                elif class_name == "Review":
                    from models.review import Review
                    FileStorage.__objects[key] = Review(**value)
                # Add additional cases here for other classes
        except FileNotFoundError:
            pass
