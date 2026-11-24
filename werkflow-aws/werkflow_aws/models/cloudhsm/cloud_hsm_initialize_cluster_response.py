from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CloudHSMInitializeClusterResponse(BaseModel):
    State: StrictStr | None = None
    StateMessage: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
