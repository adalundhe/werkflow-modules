from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class WAFv2ManagedRuleGroupVersion(BaseModel):
    Name: StrictStr | None = None
    LastUpdateTimestamp: datetime.datetime | StrictStr | None = None
