from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class LocationStartJobResponse(BaseModel):
    CreatedAt: datetime.datetime | StrictStr | None = None
    JobArn: StrictStr | None = None
    JobId: StrictStr | None = None
    Status: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
