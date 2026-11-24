from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncDeleteResolverRequest(BaseModel):
    apiId: StrictStr
    typeName: StrictStr
    fieldName: StrictStr
