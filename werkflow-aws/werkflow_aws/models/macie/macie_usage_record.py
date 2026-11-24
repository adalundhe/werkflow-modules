from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .macie_usage_by_account import MacieUsageByAccount


class MacieUsageRecord(BaseModel):
    accountId: StrictStr | None = None
    automatedDiscoveryFreeTrialStartDate: datetime.datetime | StrictStr | None = None
    freeTrialStartDate: datetime.datetime | StrictStr | None = None
    usage: list[MacieUsageByAccount] | None = None
