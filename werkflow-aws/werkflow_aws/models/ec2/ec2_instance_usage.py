from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EC2InstanceUsage(BaseModel):
    AccountId: StrictStr | None = None
    UsedInstanceCount: StrictInt | None = None
