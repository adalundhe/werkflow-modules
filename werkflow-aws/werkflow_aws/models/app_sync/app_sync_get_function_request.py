from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncGetFunctionRequest(BaseModel):
    apiId: StrictStr
    functionId: StrictStr
