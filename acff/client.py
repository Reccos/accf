import requests

class Acff(object):

    def __init__(self, sha256Hash):
        self.sha256Hash = sha256Hash
        self.version = 1
        self.url = 'https://datalake-prod2018.rbfa.be/graphql?'
        self.extensions = 'extensions={"persistedQuery":{"version":%s,"sha256Hash":"%s"}}' % (self.version, self.sha256Hash)

    def get_club_teams(self, club_id=0, language='fr'):
        url = '{}'.format(self.url)
        result = requests.get('https://datalake-prod2018.rbfa.be/graphql?operationName=getClubTeams&variables={"clubId":"%s","language":"%s"}&%s' % (club_id, 
                                                                                                                                                     language,
                                                                                                                                                     self.extensions))
        return result.json()

    def get_club_info(self, club_id=0, language='fr'):
        url = '{}'.format(self.url)
        result = requests.get('https://datalake-prod2018.rbfa.be/graphql?operationName=getClubInfo&variables={"clubId":"%s","language":"%s"}&%s' % (club_id, 
                                                                                                                                                    language,
                                                                                                                                                    self.extensions))
        return result.json()

    def get_club(self, club_id=0, language='fr'):
        url = '{}'.format(self.url)
        result = requests.get('https://datalake-prod2018.rbfa.be/graphql?operationName=getClub&variables={"clubId":"%s","language":"%s"}&%s' % (club_id, 
                                                                                                                                                language,
                                                                                                                                                 self.extensions))
        return result.json()
