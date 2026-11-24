from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFormationAccountGateResult(BaseModel):
    Status: StrictStr | None = None
    StatusReason: StrictStr | None = None
