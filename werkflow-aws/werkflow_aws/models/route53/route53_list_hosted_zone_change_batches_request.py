from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class Route53ListHostedZoneChangeBatchesRequest(BaseModel):
    HostedZoneId: StrictStr
    SubmittedAfter: StrictStr | None = None
    SubmittedBefore: StrictStr | None = None
    StartAfterChangeId: StrictStr | None = None
    SortOrder: Literal['ASCENDING', 'DESCENDING'] | None = None
    MaxResults: StrictStr | None = None
    NextToken: StrictStr | None = None
