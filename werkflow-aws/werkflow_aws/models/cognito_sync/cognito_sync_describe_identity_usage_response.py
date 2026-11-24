from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cognito_sync_identity_usage import CognitoSyncIdentityUsage


class CognitoSyncDescribeIdentityUsageResponse(BaseModel):
    IdentityUsage: CognitoSyncIdentityUsage | None = None
    ResponseMetadata: dict[str, Any] | None = None
