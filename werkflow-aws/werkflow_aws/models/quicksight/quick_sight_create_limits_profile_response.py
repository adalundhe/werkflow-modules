from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class QuickSightCreateLimitsProfileResponse(BaseModel):
    arn: StrictStr | None = None
    profileId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
