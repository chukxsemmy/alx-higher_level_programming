#!/usr/bin/python3
"""
defines Student class
"""


class Student():
    """
    Student Class
    """

    def __init__(self, first_name, last_name, age):
        """
        Constructor of a student
        Args:
          - first_name: str student firstname
          - last_name: str student lastname
          - age: int student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns the student dictionary
        Args:
          - attrs: list (None default)
        """

        result = {}

        if attrs is None:
            return (self.__dict__)

        for attr in attrs:
            value = self.__dict__.get(attr)
            if value is not None:
                result[attr] = value

        return (result)

    def reload_from_json(self, json):
        """
        updates public instance attributes
        Args:
          - json: dict
        """
        dict_des = self.__dict__

        for key, value in json.items():
            if (dict_des.get(key) == self.first_name):
                self.first_name = value
            elif (dict_des.get(key) == self.last_name):
                self.last_name = value
            elif (dict_des.get(key) == self.age):
                self.age = value
