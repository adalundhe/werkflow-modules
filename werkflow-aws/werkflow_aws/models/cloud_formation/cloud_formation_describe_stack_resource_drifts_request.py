from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class CloudFormationDescribeStackResourceDriftsRequest(BaseModel):
    StackName: StrictStr
    StackResourceDriftStatusFilters: list[Literal['IN_SYNC', 'MODIFIED', 'DELETED', 'NOT_CHECKED', 'UNKNOWN', 'UNSUPPORTED']] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
