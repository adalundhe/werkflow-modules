from __future__ import annotations
from pydantic import BaseModel, StrictStr


class STSAssumedRoleUser(BaseModel):
    AssumedRoleId: StrictStr | None = None
    Arn: StrictStr | None = None
