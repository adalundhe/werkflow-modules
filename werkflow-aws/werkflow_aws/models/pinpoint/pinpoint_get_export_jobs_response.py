from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_export_jobs_response import PinpointExportJobsResponse


class PinpointGetExportJobsResponse(BaseModel):
    ExportJobsResponse: PinpointExportJobsResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
