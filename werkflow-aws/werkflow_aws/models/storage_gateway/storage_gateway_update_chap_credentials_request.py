from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewayUpdateChapCredentialsRequest(BaseModel):
    TargetARN: StrictStr
    SecretToAuthenticateInitiator: StrictStr
    InitiatorName: StrictStr
    SecretToAuthenticateTarget: StrictStr | None = None
