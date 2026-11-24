from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class CloudTrailListDashboardsRequest(BaseModel):
    NamePrefix: StrictStr | None = None
    Type: Literal['MANAGED', 'CUSTOM'] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
