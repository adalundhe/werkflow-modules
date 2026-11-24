from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueDeleteIntegrationTablePropertiesRequest(BaseModel):
    ResourceArn: StrictStr
    TableName: StrictStr
