from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WAFv2ManagedRuleSetSummary(BaseModel):
    Name: StrictStr | None = None
    Id: StrictStr | None = None
    Description: StrictStr | None = None
    LockToken: StrictStr | None = None
    ARN: StrictStr | None = None
    LabelNamespace: StrictStr | None = None
