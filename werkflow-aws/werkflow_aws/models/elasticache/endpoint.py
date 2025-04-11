from pydantic import BaseModel, StrictStr, StrictInt


class Endpoint(BaseModel):
    Address: StrictStr
    Port: StrictInt