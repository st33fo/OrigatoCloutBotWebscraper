"""
test_messages.py - Unit test class for message container class.

@author: Jared Barrow
"""
import chat_member
import messages
import unittest
import inspect


class TestChatMember(unittest.TestCase):
    def test_module_creation(self):
        '''
        desc: Tests that the messages class is actually a class.
        '''
        test_item = chat_member.ChatMember()
        class_name = 'ChatMember' == test_item.__class__.__name__
        self.assertTrue(class_name)

    def test_user_name_getter_and_setter(self):
        '''
        desc: test user name getter and setter.
        '''
        test_item = chat_member.ChatMember()
        test_item.user_name = 'jaybarr44'
        self.assertEqual('jaybarr44', test_item.user_name)

    def test_current_messages_getter_and_setter(self):
        '''
        desc: test messages getter and setter.
        '''
        test_item = chat_member.ChatMember()
        message_1 = messages.Message(message_id=151628390)
        message_2 = messages.Message(message_id=42218969)
        message_3 = messages.Message(message_id=12323145)
        message_1.text = 'Hello chat.'
        message_2.text = 'Hi.'
        message_3.text = 'Hooray.'
        test_item.current_messages = [message_1, message_2, message_3]
        self.assertEqual(
            [message_1, message_2, message_3],
            test_item.current_messages)

    def test_get_message_by_id(self):
        '''
        desc: checks get message by id method.
        '''
        test_item = chat_member.ChatMember()
        message_1 = messages.Message(message_id=151628390)
        message_2 = messages.Message(message_id=42218969)
        message_3 = messages.Message(message_id=12323145)
        message_1.text = 'Hello chat.'
        message_2.text = 'Hi.'
        message_3.text = 'Hooray.'
        test_item.current_messages = [message_1, message_2, message_3]

        self.assertEqual('Hooray.', test_item.get_message_by_id(12323145).text)

    def test_sort_messages(self):
        '''
        desc: checks the sort messages method.
        '''
        test_item = chat_member.ChatMember()
        message_1 = messages.Message(owner_user_name='Alice')
        message_2 = messages.Message(owner_user_name='Bob')
        message_3 = messages.Message(owner_user_name='Carol')

        message_1.text = 'Hello chat.'
        message_2.text = 'Hi.'
        message_3.text = 'Hooray.'

        message_1.num_of_reacts = 3
        message_2.num_of_reacts = 1
        message_3.num_of_reacts = 2

        test_item.current_messages = [message_1, message_2, message_3]
        sorted_list = test_item.sort_messages()
        self.assertEqual(message_1.text, sorted_list[0].text)
        self.assertEqual(message_3.text, sorted_list[1].text)
        self.assertEqual(message_2.text, sorted_list[2].text)

