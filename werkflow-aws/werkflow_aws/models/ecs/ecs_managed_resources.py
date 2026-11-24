from __future__ import annotations
from pydantic import BaseModel
from .ecs_gateway_connection import ECSGatewayConnection
from .ecs_managed_auto_scaling import ECSManagedAutoScaling
from .ecs_managed_ingress_path import ECSManagedIngressPath
from .ecs_managed_log_group import ECSManagedLogGroup
from .ecs_managed_metric_alarm import ECSManagedMetricAlarm
from .ecs_managed_security_group import ECSManagedSecurityGroup


class ECSManagedResources(BaseModel):
    ingressPaths: list[ECSManagedIngressPath] | None = None
    autoScaling: ECSManagedAutoScaling | None = None
    metricAlarms: list[ECSManagedMetricAlarm] | None = None
    serviceSecurityGroups: list[ECSManagedSecurityGroup] | None = None
    logGroups: list[ECSManagedLogGroup] | None = None
    gatewayConnections: list[ECSGatewayConnection] | None = None
