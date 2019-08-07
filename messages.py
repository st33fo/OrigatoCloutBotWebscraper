"""
messages.py - Message container class.

@author: Jared Barrow
"""


class Message:
    def __init__(self, owner_user_name='', message_id=0, text='', num_of_reacts=0):
        self._owner_user_name = owner_user_name
        self._message_id = message_id
        self._text = text
        self._num_of_reacts = num_of_reacts
        self._replies = []

    @property
    def owner_user_name(self):
        return self._owner_user_name

    @owner_user_name.setter
    def owner_user_name(self, name_to_set):
        self._owner_user_name = name_to_set

    @property
    def message_id(self):
        return self._message_id

    @message_id.setter
    def message_id(self, mess_id_to_set):
        self._message_id = mess_id_to_set

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text_to_set):
        self._text = text_to_set

    @property
    def num_of_reacts(self):
        return self._num_of_reacts

    @num_of_reacts.setter
    def num_of_reacts(self, num_of_reacts_to_set):
        self._num_of_reacts = num_of_reacts_to_set

    @property
    def replies(self):
        return self._replies

    @replies.setter
    def replies(self, replies_to_set):
        self._replies = replies_to_set






