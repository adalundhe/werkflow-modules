from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class EMRGetPersistentAppUIPresignedURLResponse(BaseModel):
    PresignedURLReady: StrictBool | None = None
    PresignedURL: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
