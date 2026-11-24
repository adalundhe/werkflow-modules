from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class BatchDescribeComputeEnvironmentsRequest(BaseModel):
    computeEnvironments: list[StrictStr] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
