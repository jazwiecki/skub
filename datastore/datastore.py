# -*- coding: utf-8 -*-
"""
Persistent Data Store for use in Slack Unicode Bot
"""
import boto3
import os

from boto3.dynamodb.conditions import Key, Attr

class DataStore(object):
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb',
                                        endpoint_url = os.environ.get('DYNAMO_DB_URL'),
                                        region_name = os.environ.get('DYNAMO_DB_REGION'),
                                        aws_access_key_id = os.environ.get('CLIENT_ID'),
                                        aws_secret_access_key = os.environ.get('CLIENT_SECRET'))
        self.users = self.dynamodb.Table('Users')

    def get_user(self, team_id, user_id):
        """
        # @ String team_id
        # @ String user_id
        #
        # returns user object for combination of team_id and user_id
        """
        if team_id and user_id:
            return self.users.query(KeyConditionExpression=Key("team_user_id").eq(f'{team_id}.{user_id}'))
        else:
            raise Exception('PersistentDataStore.get_user() called with empty team or user IDs')

    def set_user(self, team_id, user_id, user_data_kwargs):
        """
        # @ String team_id
        # @ String user_id
        # @ dict user_data_kwargs
        #
        # set data to **user_data_kwargs for key team_id.user_id
        """

        if team_id and user_id:
            key = {'team_user_id': f'{team_id}.{user_id}'}
            item = {**key, **user_data_kwargs}
            self.users.put_item(Item=item)
        else:
            raise Exception('PersistentDataStore.set_user() called with empty team or user IDs')
