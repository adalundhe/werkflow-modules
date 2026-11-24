from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_export_job_request import PinpointExportJobRequest


class PinpointCreateExportJobRequest(BaseModel):
    ApplicationId: StrictStr
    ExportJobRequest: PinpointExportJobRequest
