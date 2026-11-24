from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudFormationUpdateTerminationProtectionRequest(BaseModel):
    EnableTerminationProtection: StrictBool
    StackName: StrictStr
