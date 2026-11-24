from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_job_run_summary import DataZoneJobRunSummary


class DataZoneListJobRunsResponse(BaseModel):
    items: list[DataZoneJobRunSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
