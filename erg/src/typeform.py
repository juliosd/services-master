import os
import tortilla
from typing import *

class Typeform(object):
    """
    Wrapper class for the Typeform API. 

    Usage:
    
        my_form = Typeform("12345") # where "12345" is a form id
        
    """

    db      = {} # type: Dict[str, str]
    form_id = ''
    api_key = ''


    def __init__(self) -> None:
        self.base_url = 'https://api.typeform.com/v0/'
        self.api_key  = os.environ['TYPEFORM_API_KEY']
        self.form_id  = os.environ['TYPEFORM_ID']
        self.api      = tortilla.wrap(self.base_url)

    def update_data(self) -> dict:
        "Updates the in-mem db"
        return self.api.form().get(self.form_id, params={'key': self.api_key})

    def get(self) -> dict: #, **kwargs):
        "Gets a specific item from the in-memory db"
        self.db = self.update_data()
        r = self.db.responses
        return self.db
        
        

