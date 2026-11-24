from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .macie_batch_get_custom_data_identifier_summary import MacieBatchGetCustomDataIdentifierSummary


class MacieBatchGetCustomDataIdentifiersResponse(BaseModel):
    customDataIdentifiers: list[MacieBatchGetCustomDataIdentifierSummary] | None = None
    notFoundIdentifierIds: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
