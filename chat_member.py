"""
chat_member.py - Class that represents a member of the chat.

@author: Jared Barrow
"""

import messages
from operator import attrgetter


class ChatMember:
    def __init__(self, user_name='', current_messages=[]):
        self._user_name = user_name
        self._current_messages = current_messages

    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, name_to_set):
        self._user_name = name_to_set

    @property
    def current_messages(self):
        return self._current_messages

    @current_messages.setter
    def current_messages(self, mess_to_set):
        self._current_messages = mess_to_set

    def get_message_by_id(self, mess_id=0):
        if self.current_messages:
            for message in self.current_messages:
                if message.message_id == mess_id:
                    return message
        else:
            return None
        return None

    def sort_messages(self):
        # Create a list of messages sorted by number of reacts on
        # the message.
        sorted_messages = sorted(
            self.current_messages,
            key=attrgetter('num_of_reacts'),
            reverse=True)
        return sorted_messages







