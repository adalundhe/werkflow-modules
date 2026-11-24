from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SESListExportJobsRequest(BaseModel):
    NextToken: StrictStr | None = None
    PageSize: StrictInt | None = None
    ExportSourceType: Literal['METRICS_DATA', 'MESSAGE_INSIGHTS'] | None = None
    JobStatus: Literal['CREATED', 'PROCESSING', 'COMPLETED', 'FAILED', 'CANCELLED'] | None = None
