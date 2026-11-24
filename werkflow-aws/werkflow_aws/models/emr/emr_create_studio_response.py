from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class EMRCreateStudioResponse(BaseModel):
    StudioId: StrictStr | None = None
    Url: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
