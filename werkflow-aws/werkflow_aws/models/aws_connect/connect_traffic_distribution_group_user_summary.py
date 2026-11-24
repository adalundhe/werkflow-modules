from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectTrafficDistributionGroupUserSummary(BaseModel):
    UserId: StrictStr | None = None
