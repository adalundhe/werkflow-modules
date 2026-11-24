from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ecs_express_gateway_container import ECSExpressGatewayContainer
from .ecs_express_gateway_scaling_target import ECSExpressGatewayScalingTarget
from .ecs_express_gateway_service_network_configuration import ECSExpressGatewayServiceNetworkConfiguration
from .ecs_ingress_path_summary import ECSIngressPathSummary


class ECSExpressGatewayServiceConfiguration(BaseModel):
    serviceRevisionArn: StrictStr | None = None
    executionRoleArn: StrictStr | None = None
    taskRoleArn: StrictStr | None = None
    taskDefinitionArn: StrictStr | None = None
    cpu: StrictStr | None = None
    memory: StrictStr | None = None
    cpuArchitecture: StrictStr | None = None
    networkConfiguration: ECSExpressGatewayServiceNetworkConfiguration | None = None
    healthCheckPath: StrictStr | None = None
    primaryContainer: ECSExpressGatewayContainer | None = None
    scalingTarget: ECSExpressGatewayScalingTarget | None = None
    ingressPaths: list[ECSIngressPathSummary] | None = None
    createdAt: datetime.datetime | StrictStr | None = None
