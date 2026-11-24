from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class StepFunctionsRedriveExecutionResponse(BaseModel):
    redriveDate: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
