from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ECRDescribeReplicationBackfillResultsRequest(BaseModel):
    replicationBackfillId: StrictStr
    registryId: StrictStr | None = None
    resultStatusFilter: Literal['COMPLETE', 'FAILED'] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
