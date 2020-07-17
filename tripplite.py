import requests
import json

class PDU():
    def __init__(self):
        self.authorization_token = None

    def get_auth_token(self, host, username, password):
        login_url = 'https://%s/api/AuthenticationControllers/login?password=%s&username=%s' % (host, password, username)
        response = requests.post(login_url, verify=False)
        parsed_response = json.loads(response.text)
        self.authorization_token = parsed_response['data']['token']

    def power_cycle(self, host, channel, username, password):
        self.get_auth_token(host, username, password)

        response = requests.put('https://%s/api/device/loads/%s' % (host, int(channel)),
        data = {'loadFireState':'Cycle'}, 
        verify=False,
        headers={"authorization":self.authorization_token})
        if (response.status_code == '200'):
            return True
        else:
            return False