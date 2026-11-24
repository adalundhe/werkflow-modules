from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .migration_hub_error_response import MigrationHubErrorResponse


class MigrationHubRouteSummary(BaseModel):
    AppendSourcePath: StrictBool | None = None
    ApplicationId: StrictStr | None = None
    Arn: StrictStr | None = None
    CreatedByAccountId: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    EnvironmentId: StrictStr | None = None
    Error: MigrationHubErrorResponse | None = None
    IncludeChildPaths: StrictBool | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    Methods: list[StrictStr] | None = None
    OwnerAccountId: StrictStr | None = None
    PathResourceToId: dict[StrictStr, StrictStr] | None = None
    RouteId: StrictStr | None = None
    RouteType: StrictStr | None = None
    ServiceId: StrictStr | None = None
    SourcePath: StrictStr | None = None
    State: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
