from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .migration_hub_error_response import MigrationHubErrorResponse
from .migration_hub_lambda_endpoint_config import MigrationHubLambdaEndpointConfig
from .migration_hub_url_endpoint_config import MigrationHubUrlEndpointConfig


class MigrationHubGetServiceResponse(BaseModel):
    ApplicationId: StrictStr | None = None
    Arn: StrictStr | None = None
    CreatedByAccountId: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    Description: StrictStr | None = None
    EndpointType: StrictStr | None = None
    EnvironmentId: StrictStr | None = None
    Error: MigrationHubErrorResponse | None = None
    LambdaEndpoint: MigrationHubLambdaEndpointConfig | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    Name: StrictStr | None = None
    OwnerAccountId: StrictStr | None = None
    ServiceId: StrictStr | None = None
    State: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    UrlEndpoint: MigrationHubUrlEndpointConfig | None = None
    VpcId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
