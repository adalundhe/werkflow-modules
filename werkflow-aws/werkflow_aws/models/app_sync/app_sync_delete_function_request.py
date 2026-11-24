from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncDeleteFunctionRequest(BaseModel):
    apiId: StrictStr
    functionId: StrictStr
