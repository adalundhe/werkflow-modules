from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .pinpoint_import_job_resource import PinpointImportJobResource


class PinpointImportJobResponse(BaseModel):
    ApplicationId: StrictStr | None = None
    CompletedPieces: StrictInt | None = None
    CompletionDate: StrictStr | None = None
    CreationDate: StrictStr | None = None
    Definition: PinpointImportJobResource | None = None
    FailedPieces: StrictInt | None = None
    Failures: list[StrictStr] | None = None
    Id: StrictStr | None = None
    JobStatus: StrictStr | None = None
    TotalFailures: StrictInt | None = None
    TotalPieces: StrictInt | None = None
    TotalProcessed: StrictInt | None = None
    Type: StrictStr | None = None
