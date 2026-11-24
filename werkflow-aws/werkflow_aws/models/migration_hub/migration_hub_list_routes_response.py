from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .migration_hub_route_summary import MigrationHubRouteSummary


class MigrationHubListRoutesResponse(BaseModel):
    NextToken: StrictStr | None = None
    RouteSummaryList: list[MigrationHubRouteSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
