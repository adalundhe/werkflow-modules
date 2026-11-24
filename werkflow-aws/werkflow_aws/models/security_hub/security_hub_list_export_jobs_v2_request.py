from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubListExportJobsV2Request(BaseModel):
    Status: Literal['RUNNING', 'SUCCEEDED', 'FAILED', 'CANCELLED'] | None = None
    DataType: Literal['FINDINGS'] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
