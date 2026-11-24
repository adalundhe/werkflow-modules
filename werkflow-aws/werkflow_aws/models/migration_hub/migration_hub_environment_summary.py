from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .migration_hub_error_response import MigrationHubErrorResponse


class MigrationHubEnvironmentSummary(BaseModel):
    Arn: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    Description: StrictStr | None = None
    EnvironmentId: StrictStr | None = None
    Error: MigrationHubErrorResponse | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    Name: StrictStr | None = None
    NetworkFabricType: StrictStr | None = None
    OwnerAccountId: StrictStr | None = None
    State: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    TransitGatewayId: StrictStr | None = None
