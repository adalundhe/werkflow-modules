from pydantic import BaseModel, StrictStr, StrictInt


class ConfigurationEndpoint(BaseModel):
    Address: StrictStr
    Port: StrictInt