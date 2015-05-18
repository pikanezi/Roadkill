from protorpc import remote
from protorpc.message_types import VoidMessage
from api.messages.csv_file import CsvFile

__author__ = 'Vincent'

import endpoints
from api.api import api


@api.api_class(resource_name='RoadKill', path='roadkill')
class RoadKillsEndpoint(remote.Service):
    """
    RoadKills Endpoint
    """

    @endpoints.method(name="populate", request_message=CsvFile, response_message=VoidMessage, http_method="POST")
    def populate(self):
        return VoidMessage()