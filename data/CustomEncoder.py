from data.models import *
from ratings.models import *

import json
TYPES = { 'Item': Item,
          'Outfit': Outfit }


class CustomTypeEncoder(json.JSONEncoder):
    """A custom JSONEncoder class that knows how to encode core custom
        objects.

    Custom objects are encoded as JSON object literals (ie, dicts) with
    one key, '__TypeName__' where 'TypeName' is the actual name of the
    type to which the object belongs.  That single key maps to another
    object literal which is just the __dict__ of the object encoded."""

    def default(self, obj):
        for type in TYPES.keys():
            if isinstance(obj, TYPES[type]):
                temp= obj.__dict__
                if ("_state" in temp):
                    del temp["_state"]
                return {type : temp}
        return json.JSONEncoder.default(self, obj)
