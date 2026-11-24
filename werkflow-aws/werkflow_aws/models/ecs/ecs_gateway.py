from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .ecs_describe_gateway_configuration import ECSDescribeGatewayConfiguration
from .ecs_gateway_resource_failure import ECSGatewayResourceFailure
from .ecs_tag import ECSTag


class ECSGateway(BaseModel):
    gatewayArn: StrictStr | None = None
    name: StrictStr | None = None
    status: StrictStr | None = None
    statusReason: StrictStr | None = None
    failures: list[ECSGatewayResourceFailure] | None = None
    infrastructureRoleArn: StrictStr | None = None
    deletionProtection: StrictBool | None = None
    configuration: ECSDescribeGatewayConfiguration | None = None
    accessType: StrictStr | None = None
    propagateTags: StrictStr | None = None
    tags: list[ECSTag] | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
