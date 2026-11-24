from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncGetDataSourceRequest(BaseModel):
    apiId: StrictStr
    name: StrictStr
