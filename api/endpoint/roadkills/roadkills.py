import StringIO
import csv
import logging
import urllib3
import endpoints
from protorpc import remote
from protorpc.message_types import VoidMessage
from api.models.accident import AccidentModel
from api.api import api

http = urllib3.PoolManager()

@api.api_class(resource_name='RoadKill', path='roadkill')
class RoadKillsEndpoint(remote.Service):
    """
    RoadKills Endpoint
    """

    @endpoints.method(name="populate", request_message=VoidMessage, response_message=VoidMessage, http_method="POST")
    def populate(self, request):
        r = http.request('GET', 'http://static.data.gouv.fr/fe/fea60d07a33386148deed77f826e9fe6406eae855b8620aa4a16a78362196b.csv')
        csv_file = StringIO.StringIO(r.data)
        reader = csv.reader(csv_file, delimiter=',')
        reader.next()
        for row in reader:
            accident = AccidentModel.accident_from_csv(row)
            if accident is not None:
                accident.put_async()
        csv_file.close()
        return VoidMessage()