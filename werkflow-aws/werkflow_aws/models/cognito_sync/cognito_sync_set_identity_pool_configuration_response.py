from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cognito_sync_cognito_streams import CognitoSyncCognitoStreams
from .cognito_sync_push_sync import CognitoSyncPushSync


class CognitoSyncSetIdentityPoolConfigurationResponse(BaseModel):
    IdentityPoolId: StrictStr | None = None
    PushSync: CognitoSyncPushSync | None = None
    CognitoStreams: CognitoSyncCognitoStreams | None = None
    ResponseMetadata: dict[str, Any] | None = None
