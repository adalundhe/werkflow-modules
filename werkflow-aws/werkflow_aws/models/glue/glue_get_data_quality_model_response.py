from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class GlueGetDataQualityModelResponse(BaseModel):
    Status: StrictStr | None = None
    StartedOn: datetime.datetime | StrictStr | None = None
    CompletedOn: datetime.datetime | StrictStr | None = None
    FailureReason: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
