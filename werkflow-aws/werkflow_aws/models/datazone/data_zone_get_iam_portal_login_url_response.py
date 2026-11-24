from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class DataZoneGetIamPortalLoginUrlResponse(BaseModel):
    authCodeUrl: StrictStr | None = None
    userProfileId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
