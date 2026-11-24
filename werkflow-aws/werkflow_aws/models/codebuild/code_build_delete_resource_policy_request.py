from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeBuildDeleteResourcePolicyRequest(BaseModel):
    resourceArn: StrictStr
