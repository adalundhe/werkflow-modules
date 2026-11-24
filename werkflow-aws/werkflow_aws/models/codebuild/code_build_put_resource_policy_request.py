from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeBuildPutResourcePolicyRequest(BaseModel):
    policy: StrictStr
    resourceArn: StrictStr
