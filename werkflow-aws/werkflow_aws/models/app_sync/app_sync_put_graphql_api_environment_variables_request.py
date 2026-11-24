from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncPutGraphqlApiEnvironmentVariablesRequest(BaseModel):
    apiId: StrictStr
    environmentVariables: dict[StrictStr, StrictStr]
