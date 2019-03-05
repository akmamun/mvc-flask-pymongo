from validation import Validator

class Todo(object):
    def __init__(self):
        self.validator = Validator()
        self.collection_name = 'collection_name'

        self.fields = {
            "title"     : "string",
            "body"      : "string",
            "created"   : "datatime"
        }
       self.create_required_fields = ["title", "body"]

