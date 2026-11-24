from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .kendra_index_configuration_summary import KendraIndexConfigurationSummary


class KendraListIndicesResponse(BaseModel):
    IndexConfigurationSummaryItems: list[KendraIndexConfigurationSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
