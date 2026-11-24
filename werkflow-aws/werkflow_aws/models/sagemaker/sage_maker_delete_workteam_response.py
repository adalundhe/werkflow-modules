from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool


class SageMakerDeleteWorkteamResponse(BaseModel):
    Success: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
