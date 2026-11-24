from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .macie_classification_scope_summary import MacieClassificationScopeSummary


class MacieListClassificationScopesResponse(BaseModel):
    classificationScopes: list[MacieClassificationScopeSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
