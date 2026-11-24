from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFormationSetStackPolicyRequest(BaseModel):
    StackName: StrictStr
    StackPolicyBody: StrictStr | None = None
    StackPolicyURL: StrictStr | None = None
