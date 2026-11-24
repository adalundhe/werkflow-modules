from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class WAFv2ManagedRuleGroupSummary(BaseModel):
    VendorName: StrictStr | None = None
    Name: StrictStr | None = None
    VersioningSupported: StrictBool | None = None
    Description: StrictStr | None = None
