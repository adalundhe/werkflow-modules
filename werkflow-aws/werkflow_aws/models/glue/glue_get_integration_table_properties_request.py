from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueGetIntegrationTablePropertiesRequest(BaseModel):
    ResourceArn: StrictStr
    TableName: StrictStr
