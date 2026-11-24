from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .kendra_data_source_summary import KendraDataSourceSummary


class KendraListDataSourcesResponse(BaseModel):
    SummaryItems: list[KendraDataSourceSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
