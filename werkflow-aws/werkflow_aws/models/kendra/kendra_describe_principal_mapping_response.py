from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .kendra_group_ordering_id_summary import KendraGroupOrderingIdSummary


class KendraDescribePrincipalMappingResponse(BaseModel):
    IndexId: StrictStr | None = None
    DataSourceId: StrictStr | None = None
    GroupId: StrictStr | None = None
    GroupOrderingIdSummaries: list[KendraGroupOrderingIdSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
