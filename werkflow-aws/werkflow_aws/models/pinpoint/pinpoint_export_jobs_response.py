from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_export_job_response import PinpointExportJobResponse


class PinpointExportJobsResponse(BaseModel):
    Item: list[PinpointExportJobResponse] | None = None
    NextToken: StrictStr | None = None
