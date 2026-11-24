from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_import_job_response import PinpointImportJobResponse


class PinpointImportJobsResponse(BaseModel):
    Item: list[PinpointImportJobResponse] | None = None
    NextToken: StrictStr | None = None
