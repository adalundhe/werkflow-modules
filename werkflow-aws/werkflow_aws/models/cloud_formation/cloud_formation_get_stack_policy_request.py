from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFormationGetStackPolicyRequest(BaseModel):
    StackName: StrictStr
