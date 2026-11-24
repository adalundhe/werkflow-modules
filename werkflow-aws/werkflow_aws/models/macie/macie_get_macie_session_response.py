from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class MacieGetMacieSessionResponse(BaseModel):
    createdAt: datetime.datetime | StrictStr | None = None
    findingPublishingFrequency: StrictStr | None = None
    serviceRole: StrictStr | None = None
    status: StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
