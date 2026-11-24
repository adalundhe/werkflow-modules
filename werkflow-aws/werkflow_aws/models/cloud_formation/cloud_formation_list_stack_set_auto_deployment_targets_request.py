from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class CloudFormationListStackSetAutoDeploymentTargetsRequest(BaseModel):
    StackSetName: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    CallAs: Literal['SELF', 'DELEGATED_ADMIN'] | None = None
