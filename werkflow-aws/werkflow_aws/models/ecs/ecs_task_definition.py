from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ecs_attribute import ECSAttribute
from .ecs_container_definition import ECSContainerDefinition
from .ecs_ephemeral_storage import ECSEphemeralStorage
from .ecs_inference_accelerator import ECSInferenceAccelerator
from .ecs_proxy_configuration import ECSProxyConfiguration
from .ecs_runtime_platform import ECSRuntimePlatform
from .ecs_task_definition_placement_constraint import ECSTaskDefinitionPlacementConstraint
from .ecs_trusted_execution_configuration import ECSTrustedExecutionConfiguration
from .ecs_volume import ECSVolume


class ECSTaskDefinition(BaseModel):
    taskDefinitionArn: StrictStr | None = None
    containerDefinitions: list[ECSContainerDefinition] | None = None
    family: StrictStr | None = None
    taskRoleArn: StrictStr | None = None
    executionRoleArn: StrictStr | None = None
    networkMode: StrictStr | None = None
    revision: StrictInt | None = None
    volumes: list[ECSVolume] | None = None
    status: StrictStr | None = None
    requiresAttributes: list[ECSAttribute] | None = None
    placementConstraints: list[ECSTaskDefinitionPlacementConstraint] | None = None
    compatibilities: list[StrictStr] | None = None
    runtimePlatform: ECSRuntimePlatform | None = None
    requiresCompatibilities: list[StrictStr] | None = None
    cpu: StrictStr | None = None
    memory: StrictStr | None = None
    inferenceAccelerators: list[ECSInferenceAccelerator] | None = None
    pidMode: StrictStr | None = None
    ipcMode: StrictStr | None = None
    proxyConfiguration: ECSProxyConfiguration | None = None
    registeredAt: datetime.datetime | StrictStr | None = None
    deregisteredAt: datetime.datetime | StrictStr | None = None
    deleteRequestedAt: datetime.datetime | StrictStr | None = None
    registeredBy: StrictStr | None = None
    ephemeralStorage: ECSEphemeralStorage | None = None
    enableFaultInjection: StrictBool | None = None
    trustedExecutionConfiguration: ECSTrustedExecutionConfiguration | None = None
