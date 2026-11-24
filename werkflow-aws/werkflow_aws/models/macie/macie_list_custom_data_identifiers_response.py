from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .macie_custom_data_identifier_summary import MacieCustomDataIdentifierSummary


class MacieListCustomDataIdentifiersResponse(BaseModel):
    items: list[MacieCustomDataIdentifierSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
