import unittest
from get_user_api import *

STUB_DATA = {
        1: 'George Bluth', 2: 'Janet Weaver', 3: 'Emma Wong', 4: 'Eve Holt', 5: 'Charles Morris', 6: 'Tracey Ramos', 7: 'Michael Lawson', 8: 'Lindsay Ferguson', 9: 'Tobias Funke', 10: 'Byron Fields', 11: 'George Edwards', 12: 'Rachel Howell'
}


class getUserApiTestCase(unittest.TestCase):
    def setUp(self):
        self.users = STUB_DATA

    def test_get_user_full_name_list(self):
        l = get_user_full_name_list(1, 3, self.users)
        assert l == ['Emma Wong', 'George Bluth', 'Janet Weaver']

    def test_get_user_full_name_list_all(self):
        l = get_user_full_name_list(1, 12, self.users)
        assert l == ['Byron Fields', 'Charles Morris', 'Emma Wong', 'Eve Holt', 'George Bluth', 'George Edwards', 'Janet Weaver', 'Lindsay Ferguson', 'Michael Lawson', 'Rachel Howell', 'Tobias Funke', 'Tracey Ramos']

    def test_get_user_full_name_list_start_out_of_range(self):
        l = get_user_full_name_list(-1, 5, self.users)
        assert l == []

    def test_get_user_full_name_list_end_out_of_range(self):
        l = get_user_full_name_list(10, 100, self.users)
        assert l == []

    def test_get_user_full_name_list_float_input(self):
        l = get_user_full_name_list(1.5, 7, self.users)
        assert l == []

    def test_get_user_full_name_list_string_input(self):
        l = get_user_full_name_list(9, '12', self.users)
        assert l == []

    def test_get_user_full_name_list_end_larger_than_start(self):
        l = get_user_full_name_list(10, 4, self.users)
        assert l == []

if __name__ == '__main__':
    unittest.main()
