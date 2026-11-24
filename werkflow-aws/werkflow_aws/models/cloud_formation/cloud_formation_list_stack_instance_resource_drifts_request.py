from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class CloudFormationListStackInstanceResourceDriftsRequest(BaseModel):
    StackSetName: StrictStr
    StackInstanceAccount: StrictStr
    StackInstanceRegion: StrictStr
    OperationId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    StackInstanceResourceDriftStatuses: list[Literal['IN_SYNC', 'MODIFIED', 'DELETED', 'NOT_CHECKED', 'UNKNOWN', 'UNSUPPORTED']] | None = None
    CallAs: Literal['SELF', 'DELEGATED_ADMIN'] | None = None
