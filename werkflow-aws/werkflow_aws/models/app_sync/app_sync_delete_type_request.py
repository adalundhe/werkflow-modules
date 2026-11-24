from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncDeleteTypeRequest(BaseModel):
    apiId: StrictStr
    typeName: StrictStr
