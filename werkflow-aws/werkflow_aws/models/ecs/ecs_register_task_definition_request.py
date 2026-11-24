from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .ecs_container_definition import ECSContainerDefinition
from .ecs_ephemeral_storage import ECSEphemeralStorage
from .ecs_inference_accelerator import ECSInferenceAccelerator
from .ecs_proxy_configuration import ECSProxyConfiguration
from .ecs_runtime_platform import ECSRuntimePlatform
from .ecs_tag import ECSTag
from .ecs_task_definition_placement_constraint import ECSTaskDefinitionPlacementConstraint
from .ecs_trusted_execution_configuration import ECSTrustedExecutionConfiguration
from .ecs_volume import ECSVolume


class ECSRegisterTaskDefinitionRequest(BaseModel):
    family: StrictStr
    containerDefinitions: list[ECSContainerDefinition]
    taskRoleArn: StrictStr | None = None
    executionRoleArn: StrictStr | None = None
    networkMode: Literal['bridge', 'host', 'awsvpc', 'none'] | None = None
    volumes: list[ECSVolume] | None = None
    placementConstraints: list[ECSTaskDefinitionPlacementConstraint] | None = None
    requiresCompatibilities: list[Literal['EC2', 'FARGATE', 'EXTERNAL', 'MANAGED_INSTANCES']] | None = None
    cpu: StrictStr | None = None
    memory: StrictStr | None = None
    tags: list[ECSTag] | None = None
    pidMode: Literal['host', 'task'] | None = None
    ipcMode: Literal['host', 'task', 'none'] | None = None
    proxyConfiguration: ECSProxyConfiguration | None = None
    inferenceAccelerators: list[ECSInferenceAccelerator] | None = None
    ephemeralStorage: ECSEphemeralStorage | None = None
    runtimePlatform: ECSRuntimePlatform | None = None
    enableFaultInjection: StrictBool | None = None
    trustedExecutionConfiguration: ECSTrustedExecutionConfiguration | None = None
