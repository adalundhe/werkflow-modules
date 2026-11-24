from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cognito_sync_identity_pool_usage import CognitoSyncIdentityPoolUsage


class CognitoSyncDescribeIdentityPoolUsageResponse(BaseModel):
    IdentityPoolUsage: CognitoSyncIdentityPoolUsage | None = None
    ResponseMetadata: dict[str, Any] | None = None
