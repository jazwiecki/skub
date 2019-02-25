import boto3
import datastore
import unittest

from moto import mock_dynamodb2

class TestDataStore(unittest.TestCase):

    def setUp(self):
        # dynamodb = boto3.resource('dynamodb')
        self.datastore = datastore.DataStore()


    @mock_dynamodb2
    def testSetNewUser(self):
        dynamodb = boto3.resource('dynamodb', 'us-east-1')
        table = dynamodb.create_table(
            TableName='Users',
            KeySchema=[
                {
                    'AttributeName': 'team_user_id',
                    'KeyType': 'HASH'
                },
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'team_user_id',
                    'AttributeType': 'S'
                },

            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )

        team_id = 'test_team_id'
        user_id = 'test_user_id'
        # team_user_id = f'{team_id}.{user_id}'
        team_user_auth_token = 'team1.user1.auth_token'
        test_user_data = {
                        'auth_token': team_user_auth_token
        }
        self.datastore.set_user(team_id, user_id, test_user_data)
        test_query_results = self.datastore.get_user(team_id, user_id)

        # set/fetched auth tokens should equal
        test_user = test_query_results['Item']
        assert test_user['auth_token'] == team_user_auth_token

    @mock_dynamodb2
    def testUpdateOrCreateUser(self):
        dynamodb = boto3.resource('dynamodb', 'us-east-1')
        table = dynamodb.create_table(
            TableName='Users',
            KeySchema=[
                {
                    'AttributeName': 'team_user_id',
                    'KeyType': 'HASH'
                },
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'team_user_id',
                    'AttributeType': 'S'
                },

            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )

        assert False