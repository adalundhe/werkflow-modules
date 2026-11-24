from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_job_execution_summary_for_thing import IoTJobExecutionSummaryForThing


class IoTListJobExecutionsForThingResponse(BaseModel):
    executionSummaries: list[IoTJobExecutionSummaryForThing] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
