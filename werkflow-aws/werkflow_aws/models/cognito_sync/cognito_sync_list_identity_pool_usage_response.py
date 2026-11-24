from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .cognito_sync_identity_pool_usage import CognitoSyncIdentityPoolUsage


class CognitoSyncListIdentityPoolUsageResponse(BaseModel):
    IdentityPoolUsages: list[CognitoSyncIdentityPoolUsage] | None = None
    MaxResults: StrictInt | None = None
    Count: StrictInt | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
