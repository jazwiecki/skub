import datastore
import unittest

from moto import mock_dynamodb2

class TestDataStore(unittest.TestCase):

    def setUp(self):
        self.datastore = datastore.DataStore()

    @mock_dynamodb2
    def testSetNewUser(self):
        team_id = 'test_team_id'
        user_id = 'test_user_id'
        team_user_auth_token = 'team1.user1.auth_token'
        test_user_data = {
                        'auth_token': team_user_auth_token
        }
        self.datastore.set_user(team_id, user_id, test_user_data)
        test_query_results = self.datastore.get_user(team_user_id)

        # should be only one! TODO: add test

        # auth tokens should equal
        test_user = test_query_results['Item']
        assert test_user.auth_token == team_user_auth_token
        assert False == True