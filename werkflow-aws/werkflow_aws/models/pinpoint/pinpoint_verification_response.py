from __future__ import annotations
from pydantic import BaseModel, StrictBool


class PinpointVerificationResponse(BaseModel):
    Valid: StrictBool | None = None
