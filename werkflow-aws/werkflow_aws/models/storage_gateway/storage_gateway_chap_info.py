from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewayChapInfo(BaseModel):
    TargetARN: StrictStr | None = None
    SecretToAuthenticateInitiator: StrictStr | None = None
    InitiatorName: StrictStr | None = None
    SecretToAuthenticateTarget: StrictStr | None = None
