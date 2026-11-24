from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesIpRuleItem(BaseModel):
    ipRule: StrictStr | None = None
    ruleDesc: StrictStr | None = None
