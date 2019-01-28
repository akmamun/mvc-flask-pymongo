from datetime import datetime


class Validator(object):
   def validate_type(self, element, desired_type):
       if desired_type == 'int':
           return type(element) == int
       if desired_type == 'str':
           return type(element) == str
       if desired_type == 'float':
           return type(element) == float     
       if desired_type == 'datetime':
           return isinstance(element, type)   
       if type(desired_type) == list  
         return (element in desired_type)
       raise ValueError("Invalid value for desired type")

    def validateTypes(self, element, fields):
    for field in fields:
        if field in element:
            if self.validate_type(element[field], fields[field]):
                return True
