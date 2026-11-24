from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class LightsailCheckSubdomainAvailabilityResponse(BaseModel):
    available: StrictBool | None = None
    reservationExpiresAt: datetime.datetime | StrictStr | None = None
    subdomainName: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
