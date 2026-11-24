from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cognito_sync_cognito_streams import CognitoSyncCognitoStreams
from .cognito_sync_push_sync import CognitoSyncPushSync


class CognitoSyncSetIdentityPoolConfigurationRequest(BaseModel):
    IdentityPoolId: StrictStr
    PushSync: CognitoSyncPushSync | None = None
    CognitoStreams: CognitoSyncCognitoStreams | None = None
