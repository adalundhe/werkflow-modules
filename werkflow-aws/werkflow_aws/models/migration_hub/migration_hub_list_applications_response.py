from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .migration_hub_application_summary import MigrationHubApplicationSummary


class MigrationHubListApplicationsResponse(BaseModel):
    ApplicationSummaryList: list[MigrationHubApplicationSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
