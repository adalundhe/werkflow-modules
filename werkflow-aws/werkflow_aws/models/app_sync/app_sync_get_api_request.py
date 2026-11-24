from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncGetApiRequest(BaseModel):
    apiId: StrictStr
