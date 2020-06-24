import requests
from utils.user_agents.client import UserAgent
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
import asyncio

class Acff(object):

    def __init__(self, sha256Hash):
        self.sha256Hash = sha256Hash
        self.version = 1
        self.url = 'https://datalake-prod2018.rbfa.be/graphql'
        self.extensions = 'extensions={"persistedQuery":{"version":%s,"sha256Hash":"%s"}' % (self.version, self.sha256Hash)

    def get_club_teams(self, club_id=0, language='fr'):
        result = requests.get('%s?operationName=getClubTeams&variables={"clubId":"%s","language":"%s"}&%s}' % (self.url,
                                                                                                               club_id, 
                                                                                                               language,
                                                                                                               self.extensions))
        return result.json()

    def get_club_info(self, club_id=0, language='fr'):
        result = requests.get('%s?operationName=getClubInfo&variables={"clubId":"%s","language":"%s"}&%s}' % (self.url,
                                                                                                              club_id, 
                                                                                                              language,
                                                                                                              self.extensions))
        return result.json()

    def get_club(self, club_id=0, language='fr'):
        result = requests.get('%s?operationName=getClub&variables={"clubId":"%s","language":"%s"}&%s}' % (self.url,
                                                                                                          club_id, 
                                                                                                          language,
                                                                                                          self.extensions))
        return result.json()

    def get_games(self, series_id, start_date, end_date, language='fr'):
        result = requests.get('%s?operationName=GetSeriesCalendar&variables={"seriesId":"%s","startDate":"%s","endDate":"%s","language":"%s"}&%s}' % (self.url,
                                                                                                                                                      series_id, 
                                                                                                                                                      start_date,
                                                                                                                                                      end_date,
                                                                                                                                                      language,
                                                                                                                                                      self.extensions))
        return result.json()
