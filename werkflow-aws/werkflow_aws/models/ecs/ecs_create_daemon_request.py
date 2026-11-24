from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .ecs_daemon_deployment_configuration import ECSDaemonDeploymentConfiguration
from .ecs_tag import ECSTag


class ECSCreateDaemonRequest(BaseModel):
    daemonName: StrictStr
    daemonTaskDefinitionArn: StrictStr
    capacityProviderArns: list[StrictStr]
    clusterArn: StrictStr | None = None
    deploymentConfiguration: ECSDaemonDeploymentConfiguration | None = None
    tags: list[ECSTag] | None = None
    propagateTags: Literal['DAEMON', 'NONE'] | None = None
    enableECSManagedTags: StrictBool | None = None
    enableExecuteCommand: StrictBool | None = None
    clientToken: StrictStr | None = None
    critical: StrictBool | None = None
