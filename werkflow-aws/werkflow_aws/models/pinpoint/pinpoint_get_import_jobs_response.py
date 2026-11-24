from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_import_jobs_response import PinpointImportJobsResponse


class PinpointGetImportJobsResponse(BaseModel):
    ImportJobsResponse: PinpointImportJobsResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
