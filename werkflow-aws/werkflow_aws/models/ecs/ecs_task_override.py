from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecs_container_override import ECSContainerOverride
from .ecs_ephemeral_storage import ECSEphemeralStorage
from .ecs_inference_accelerator_override import ECSInferenceAcceleratorOverride


class ECSTaskOverride(BaseModel):
    containerOverrides: list[ECSContainerOverride] | None = None
    cpu: StrictStr | None = None
    inferenceAcceleratorOverrides: list[ECSInferenceAcceleratorOverride] | None = None
    executionRoleArn: StrictStr | None = None
    memory: StrictStr | None = None
    taskRoleArn: StrictStr | None = None
    ephemeralStorage: ECSEphemeralStorage | None = None
