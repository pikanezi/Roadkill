import endpoints

from config import CLIENT_IDS, AUDIENCES

api = endpoints.api(name='roadkills', version='v1',
                    allowed_client_ids=CLIENT_IDS,
                    audiences=AUDIENCES)
