from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DevOpsGuruDescribeAnomalyRequest(BaseModel):
    Id: StrictStr
    AccountId: StrictStr | None = None
