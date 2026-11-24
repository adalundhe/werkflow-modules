from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class SSMPutParameterResponse(BaseModel):
    Version: StrictInt | None = None
    Tier: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
