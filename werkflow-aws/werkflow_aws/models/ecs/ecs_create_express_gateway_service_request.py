from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .ecs_express_gateway_container import ECSExpressGatewayContainer
from .ecs_express_gateway_scaling_target import ECSExpressGatewayScalingTarget
from .ecs_express_gateway_service_network_configuration import ECSExpressGatewayServiceNetworkConfiguration
from .ecs_tag import ECSTag


class ECSCreateExpressGatewayServiceRequest(BaseModel):
    infrastructureRoleArn: StrictStr
    executionRoleArn: StrictStr | None = None
    serviceName: StrictStr | None = None
    cluster: StrictStr | None = None
    healthCheckPath: StrictStr | None = None
    primaryContainer: ECSExpressGatewayContainer | None = None
    taskRoleArn: StrictStr | None = None
    networkConfiguration: ECSExpressGatewayServiceNetworkConfiguration | None = None
    cpu: StrictStr | None = None
    memory: StrictStr | None = None
    cpuArchitecture: Literal['X86_64', 'ARM64'] | None = None
    scalingTarget: ECSExpressGatewayScalingTarget | None = None
    tags: list[ECSTag] | None = None
    taskDefinitionArn: StrictStr | None = None
