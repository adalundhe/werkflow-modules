from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_import_job_response import PinpointImportJobResponse


class PinpointCreateImportJobResponse(BaseModel):
    ImportJobResponse: PinpointImportJobResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
