from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncDeleteDataSourceRequest(BaseModel):
    apiId: StrictStr
    name: StrictStr
