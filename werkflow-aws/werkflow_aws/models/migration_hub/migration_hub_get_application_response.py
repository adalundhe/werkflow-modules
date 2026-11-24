from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .migration_hub_api_gateway_proxy_config import MigrationHubApiGatewayProxyConfig
from .migration_hub_error_response import MigrationHubErrorResponse


class MigrationHubGetApplicationResponse(BaseModel):
    ApiGatewayProxy: MigrationHubApiGatewayProxyConfig | None = None
    ApplicationId: StrictStr | None = None
    Arn: StrictStr | None = None
    CreatedByAccountId: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    EnvironmentId: StrictStr | None = None
    Error: MigrationHubErrorResponse | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    Name: StrictStr | None = None
    OwnerAccountId: StrictStr | None = None
    ProxyType: StrictStr | None = None
    State: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    VpcId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
