from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .macie_allow_list_criteria import MacieAllowListCriteria


class MacieUpdateAllowListRequest(BaseModel):
    criteria: MacieAllowListCriteria
    id: StrictStr
    name: StrictStr
    description: StrictStr | None = None
