from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .ecs_daemon_deployment_configuration import ECSDaemonDeploymentConfiguration


class ECSUpdateDaemonRequest(BaseModel):
    daemonArn: StrictStr
    daemonTaskDefinitionArn: StrictStr
    capacityProviderArns: list[StrictStr]
    deploymentConfiguration: ECSDaemonDeploymentConfiguration | None = None
    propagateTags: Literal['DAEMON', 'NONE'] | None = None
    enableECSManagedTags: StrictBool | None = None
    enableExecuteCommand: StrictBool | None = None
    critical: StrictBool | None = None
