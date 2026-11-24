from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .migration_hub_lambda_endpoint_input import MigrationHubLambdaEndpointInput
from .migration_hub_url_endpoint_input import MigrationHubUrlEndpointInput


class MigrationHubCreateServiceRequest(BaseModel):
    ApplicationIdentifier: StrictStr
    EndpointType: Literal['LAMBDA', 'URL']
    EnvironmentIdentifier: StrictStr
    Name: StrictStr
    ClientToken: StrictStr | None = None
    Description: StrictStr | None = None
    LambdaEndpoint: MigrationHubLambdaEndpointInput | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    UrlEndpoint: MigrationHubUrlEndpointInput | None = None
    VpcId: StrictStr | None = None
