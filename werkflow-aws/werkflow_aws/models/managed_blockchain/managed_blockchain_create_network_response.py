from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ManagedBlockchainCreateNetworkResponse(BaseModel):
    NetworkId: StrictStr | None = None
    MemberId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
