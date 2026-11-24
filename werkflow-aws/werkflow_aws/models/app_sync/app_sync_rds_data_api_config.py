from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncRdsDataApiConfig(BaseModel):
    resourceArn: StrictStr
    secretArn: StrictStr
    databaseName: StrictStr
