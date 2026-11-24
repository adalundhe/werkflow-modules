from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .ecs_network_configuration import ECSNetworkConfiguration
from .ecs_tag import ECSTag
from .ecs_task_override import ECSTaskOverride
from .ecs_task_volume_configuration import ECSTaskVolumeConfiguration


class ECSStartTaskRequest(BaseModel):
    containerInstances: list[StrictStr]
    taskDefinition: StrictStr
    cluster: StrictStr | None = None
    enableECSManagedTags: StrictBool | None = None
    enableExecuteCommand: StrictBool | None = None
    group: StrictStr | None = None
    networkConfiguration: ECSNetworkConfiguration | None = None
    overrides: ECSTaskOverride | None = None
    propagateTags: Literal['TASK_DEFINITION', 'SERVICE', 'NONE'] | None = None
    referenceId: StrictStr | None = None
    startedBy: StrictStr | None = None
    tags: list[ECSTag] | None = None
    volumeConfigurations: list[ECSTaskVolumeConfiguration] | None = None
