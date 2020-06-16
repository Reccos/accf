import requests, json


class Acff(object):

    def __init__(self, sha256Hash):
        self.sha256Hash = sha256Hash
        self.version = 1
        self.url = 'https://datalake-prod2018.rbfa.be/graphql?'

    def operation_name(self, variables={}):
        extensions = {
            'persistedQuery': {
                'version': self.version,
                'sha256Hash': self.sha256Hash
            }  
        }
        url = '{}operationName=getClubInfo&variables={}&extensions={}'.format(self.url, variables, extensions)
        result = requests.get(url)
        return result.json()

    def get_legal_navigation_for_channel(self, variables={}):
        extensions = {
            'persistedQuery': {
                'version': self.version,
                'sha256Hash': self.sha256Hash
            }  
        }
        url = '{}operationName=GetLegalNavigationForChannel&variables={}&extensions={}'.format(self.url, variables, extensions)
        result = requests.get(url)
        return result.json()