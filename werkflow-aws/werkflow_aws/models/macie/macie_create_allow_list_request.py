from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .macie_allow_list_criteria import MacieAllowListCriteria


class MacieCreateAllowListRequest(BaseModel):
    clientToken: StrictStr
    criteria: MacieAllowListCriteria
    name: StrictStr
    description: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
