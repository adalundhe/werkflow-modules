from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class Route53UpdateTrafficPolicyCommentRequest(BaseModel):
    Id: StrictStr
    Version: StrictInt
    Comment: StrictStr
