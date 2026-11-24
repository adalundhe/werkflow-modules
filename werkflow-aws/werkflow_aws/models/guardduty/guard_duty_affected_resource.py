from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyAffectedResource(BaseModel):
    Identifier: StrictStr | None = None
    Type: StrictStr | None = None
    Arn: StrictStr | None = None
