from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ecs_environment_file import ECSEnvironmentFile
from .ecs_key_value_pair import ECSKeyValuePair
from .ecs_resource_requirement import ECSResourceRequirement


class ECSContainerOverride(BaseModel):
    name: StrictStr | None = None
    command: list[StrictStr] | None = None
    environment: list[ECSKeyValuePair] | None = None
    environmentFiles: list[ECSEnvironmentFile] | None = None
    cpu: StrictInt | None = None
    memory: StrictInt | None = None
    memoryReservation: StrictInt | None = None
    resourceRequirements: list[ECSResourceRequirement] | None = None
