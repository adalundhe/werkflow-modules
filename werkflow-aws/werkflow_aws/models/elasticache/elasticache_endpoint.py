from pydantic import BaseModel, StrictStr, StrictInt


class ElasticacheEndpoint(BaseModel):
    Address: StrictStr
    Port: StrictInt