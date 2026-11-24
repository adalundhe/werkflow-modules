from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class StepFunctionsStartExecutionResponse(BaseModel):
    executionArn: StrictStr | None = None
    startDate: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
