from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerCoreNetworkPolicyError(BaseModel):
    ErrorCode: StrictStr | None = None
    Message: StrictStr | None = None
    Path: StrictStr | None = None
