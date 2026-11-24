from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .migration_hub_environment_summary import MigrationHubEnvironmentSummary


class MigrationHubListEnvironmentsResponse(BaseModel):
    EnvironmentSummaryList: list[MigrationHubEnvironmentSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
