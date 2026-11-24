from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncGetGraphqlApiRequest(BaseModel):
    apiId: StrictStr
