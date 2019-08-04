"""
test_messages.py - Unit test class for message container class.

@author: Jared Barrow
"""
import messages
import unittest
import inspect


class TestMessages(unittest.TestCase):
    def test_module_creation(self):
        '''
        desc: Tests that the messages class is actually a class.
        '''
        test_item = messages.Message()
        class_name = 'Message' == test_item.__class__.__name__
        self.assertTrue(class_name)

    def test_owner_id_getter_and_setter(self):
        '''
        desc: test owner id getter and setter.
        '''
        test_item = messages.Message()
        test_item.owner_id = 2042
        self.assertEqual(2042, test_item.owner_id)

    def test_message_id_getter_and_setter(self):
        '''
        desc: test message id getter and setter.
        '''
        test_item = messages.Message()
        test_item.message_id = 2042
        self.assertEqual(2042, test_item.message_id)

    def test_text_getter_and_setter(self):
        '''
        desc: test text id getter and setter.
        '''
        test_item = messages.Message()
        test_text = 'Doin a lil bit of modeling population dynamics ' \
                    'seems fun but would need to improve my math ' \
                    'background a lot for that kinda shiz'
        test_item.text = test_text
        self.assertEqual(test_text, test_item.text)

    def test_reacts_getter_and_setter(self):
        '''
        desc: test reacts getter and setter.
        '''
        test_item = messages.Message()
        test_item.reacts = 3
        self.assertEqual(3, test_item.reacts)

    def test_replies_getter_and_setter(self):
        '''
        desc: test replies getter and setter.
        '''
        test_item = messages.Message()
        test_replies = [
            'I like the nature',
            '''Guess confidence is one of the most important 
            leadership qualities lol''',
            'How many days there do you have left']
        test_item.replies = test_replies
        self.assertEqual(test_replies, test_item.replies)


if __name__ == '__main__':
    unittest.main()

