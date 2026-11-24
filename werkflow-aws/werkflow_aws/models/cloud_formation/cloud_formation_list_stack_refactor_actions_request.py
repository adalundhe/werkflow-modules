from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudFormationListStackRefactorActionsRequest(BaseModel):
    StackRefactorId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
