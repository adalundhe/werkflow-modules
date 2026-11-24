from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncGetResolverRequest(BaseModel):
    apiId: StrictStr
    typeName: StrictStr
    fieldName: StrictStr
