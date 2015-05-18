import endpoints
from endpoint.roadkills import RoadKillsEndpoints

APPLICATION = endpoints.api_server(RoadKillsEndpoints)