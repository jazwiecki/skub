import bot
import json
import mock
import uniform
import unittest

def slack_oauth_access(client_id, client_secret, code):
    """
    pass in user id, team id, and code, get back mocked JSON
    with user id, team id, and token
    """
    mocked_auth_response = {
        'ok': True,
        'access_token': '.'.join((client_id, client_secret, code)),
        'user_id': client_id,
        'team_id': client_secret,
    }
    return json.dumps(mocked_auth_response)


class TestBot(unittest.TestCase):

    def setUp(self):
        self.pyBot = bot.Bot()
        self.slack = self.pyBot.client

    @mock.patch('slackclient.SlackClient.api_call', side_effect=slack_oauth_access)
    def test_same_team_multiple_user_auth(self, patched_oauth_access):
        """
        test that we can set/retrieve the right user token for users
        on the same team
        """

        user_1_code = "user_1_code"
        user_2_code = "user_2_code"

        # expected return values
        team_id = "test_team"
        user_1_id = "user_1"
        user_2_id = "user_2"
        user_1_token = "user_1.test_team.user_1_code"
        user_2_token = "user_2.test_team.user_2_code"

        mocked_auth_response = json.loads(self.slack.api_call(user_1_id, team_id, user_1_code))
        assert mocked_auth_response['access_token'] == user_1_token

        mocked_auth_response = json.loads(self.slack.api_call(user_2_id, team_id, user_2_code))
        assert mocked_auth_response['access_token'] == user_2_token

        # TODO: retrieve correct token for user id
