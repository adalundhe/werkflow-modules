from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_import_job_request import PinpointImportJobRequest


class PinpointCreateImportJobRequest(BaseModel):
    ApplicationId: StrictStr
    ImportJobRequest: PinpointImportJobRequest
