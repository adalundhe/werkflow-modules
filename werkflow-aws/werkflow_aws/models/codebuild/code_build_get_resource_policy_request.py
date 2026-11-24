from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeBuildGetResourcePolicyRequest(BaseModel):
    resourceArn: StrictStr
