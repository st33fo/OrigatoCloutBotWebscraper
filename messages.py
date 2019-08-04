"""
messages.py - Message container class.

@author: Jared Barrow
"""


class Message:
    def __init__(self, owner_id=0, text='', reacts=0):
        self.owner_id = owner_id
        self._text = text
        self._reacts = reacts
        self._replies = []

    @property
    def owner_id(self):
        return self._owner_id

    @owner_id.setter
    def owner_id(self, id_to_set):
        self._owner_id = id_to_set

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text_to_set):
        self._text = text_to_set

    @property
    def reacts(self):
        return self._reacts

    @reacts.setter
    def reacts(self, reacts_to_set):
        self._reacts = reacts_to_set

    @property
    def replies(self):
        return self._replies

    @replies.setter
    def replies(self, replies_to_set):
        self._replies = replies_to_set




