from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class LakeFormationGetQueryStateResponse(BaseModel):
    Error: StrictStr | None = None
    State: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
