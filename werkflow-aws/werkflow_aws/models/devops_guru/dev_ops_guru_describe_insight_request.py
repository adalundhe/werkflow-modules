from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DevOpsGuruDescribeInsightRequest(BaseModel):
    Id: StrictStr
    AccountId: StrictStr | None = None
