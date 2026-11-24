from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceDisassociateResourceTypesRequest(BaseModel):
    ConfigurationRecorderArn: StrictStr
    ResourceTypes: list[StrictStr]
