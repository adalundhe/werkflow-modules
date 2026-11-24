from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class CloudTrailListImportsRequest(BaseModel):
    MaxResults: StrictInt | None = None
    Destination: StrictStr | None = None
    ImportStatus: Literal['INITIALIZING', 'IN_PROGRESS', 'FAILED', 'STOPPED', 'COMPLETED'] | None = None
    NextToken: StrictStr | None = None
