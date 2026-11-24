from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .migration_hub_environment_vpc import MigrationHubEnvironmentVpc


class MigrationHubListEnvironmentVpcsResponse(BaseModel):
    EnvironmentVpcList: list[MigrationHubEnvironmentVpc] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
