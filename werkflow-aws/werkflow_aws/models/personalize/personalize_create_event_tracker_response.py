from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class PersonalizeCreateEventTrackerResponse(BaseModel):
    eventTrackerArn: StrictStr | None = None
    trackingId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
