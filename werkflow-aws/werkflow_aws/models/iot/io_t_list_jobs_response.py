from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_job_summary import IoTJobSummary


class IoTListJobsResponse(BaseModel):
    jobs: list[IoTJobSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
