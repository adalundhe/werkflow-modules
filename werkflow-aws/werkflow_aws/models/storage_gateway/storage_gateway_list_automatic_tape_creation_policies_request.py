from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewayListAutomaticTapeCreationPoliciesRequest(BaseModel):
    GatewayARN: StrictStr | None = None
