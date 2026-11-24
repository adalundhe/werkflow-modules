from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFormationListChangeSetsRequest(BaseModel):
    StackName: StrictStr
    NextToken: StrictStr | None = None
