from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .migration_hub_service_summary import MigrationHubServiceSummary


class MigrationHubListServicesResponse(BaseModel):
    NextToken: StrictStr | None = None
    ServiceSummaryList: list[MigrationHubServiceSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
