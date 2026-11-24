from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .macie_findings_filter_list_item import MacieFindingsFilterListItem


class MacieListFindingsFiltersResponse(BaseModel):
    findingsFilterListItems: list[MacieFindingsFilterListItem] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
