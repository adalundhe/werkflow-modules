from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMPolicyDetail(BaseModel):
    PolicyName: StrictStr | None = None
    PolicyDocument: StrictStr | None = None
