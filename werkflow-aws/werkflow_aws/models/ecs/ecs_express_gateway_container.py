from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ecs_express_gateway_repository_credentials import ECSExpressGatewayRepositoryCredentials
from .ecs_express_gateway_service_aws_logs_configuration import ECSExpressGatewayServiceAwsLogsConfiguration
from .ecs_key_value_pair import ECSKeyValuePair
from .ecs_secret import ECSSecret


class ECSExpressGatewayContainer(BaseModel):
    image: StrictStr | None = None
    containerPort: StrictInt | None = None
    awsLogsConfiguration: ECSExpressGatewayServiceAwsLogsConfiguration | None = None
    repositoryCredentials: ECSExpressGatewayRepositoryCredentials | None = None
    command: list[StrictStr] | None = None
    environment: list[ECSKeyValuePair] | None = None
    secrets: list[ECSSecret] | None = None
