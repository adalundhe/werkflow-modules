from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class IAMCreatePolicyVersionRequest(BaseModel):
    PolicyArn: StrictStr
    PolicyDocument: StrictStr
    SetAsDefault: StrictBool | None = None
