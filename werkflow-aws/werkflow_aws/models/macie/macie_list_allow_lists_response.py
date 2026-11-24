from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .macie_allow_list_summary import MacieAllowListSummary


class MacieListAllowListsResponse(BaseModel):
    allowLists: list[MacieAllowListSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
