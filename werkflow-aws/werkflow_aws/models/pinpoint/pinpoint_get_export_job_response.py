from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_export_job_response import PinpointExportJobResponse


class PinpointGetExportJobResponse(BaseModel):
    ExportJobResponse: PinpointExportJobResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
