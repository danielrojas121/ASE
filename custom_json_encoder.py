"""Python file containing custom JSON encoding/decoding classes"""

import json
from flask.json import JSONEncoder, JSONDecoder
from user import User
from account import Account

class CustomJSONEncoder(JSONEncoder):
    """Custom JSON encoder to serialize User and Account objects"""
    def default(self, obj): # pylint: disable=E0202
        """Handle different object instances"""
        if isinstance(obj, User):
            #implement code to convert User object to a dict
            user_dict = {}
            user_dict['id'] = obj.get_user_id()
            user_dict['username'] = obj.get_username()
            user_dict['accounts'] = obj.get_accounts()
            return user_dict
        elif isinstance(obj, Account):
            #Implement custom code for Account objects
            JSONEncoder.default(self, obj)
        else:
            JSONEncoder.default(self, obj)

class CustomJSONDecoder(JSONDecoder):
    """Custom JSON decoder to deserialize User and Account objects"""
    def __init__(self, *args, **kwargs):
        """Initialize JSON decoder & call custom decoding functions"""
        self.orig_obj_hook = kwargs.pop("object_hook", None)
        super(CustomJSONDecoder, self).__init__(*args, object_hook=self.custom_obj_hook,
                                                **kwargs)

    def custom_obj_hook(self, dictionary):
        """custom decode function"""
        dictionary = self.decode(dictionary)
        if self.orig_obj_hook:
            return self.orig_obj_hook(dictionary)
        return dictionary # Return decoded hook if no other hook

    def decode(self, dictionary):
        """Load JSON string into a dictionary object"""
        dictionary = json.loads(dictionary)
        return dictionary
