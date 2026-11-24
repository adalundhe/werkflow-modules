from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .macie_managed_data_identifier_summary import MacieManagedDataIdentifierSummary


class MacieListManagedDataIdentifiersResponse(BaseModel):
    items: list[MacieManagedDataIdentifierSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
