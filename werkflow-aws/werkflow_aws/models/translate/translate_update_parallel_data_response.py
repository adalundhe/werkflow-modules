from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class TranslateUpdateParallelDataResponse(BaseModel):
    Name: StrictStr | None = None
    Status: StrictStr | None = None
    LatestUpdateAttemptStatus: StrictStr | None = None
    LatestUpdateAttemptAt: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
