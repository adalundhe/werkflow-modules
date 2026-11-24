from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceAssociateResourceTypesRequest(BaseModel):
    ConfigurationRecorderArn: StrictStr
    ResourceTypes: list[StrictStr]
