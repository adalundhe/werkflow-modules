from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ecs_attachment import ECSAttachment
from .ecs_attribute import ECSAttribute
from .ecs_container import ECSContainer
from .ecs_ephemeral_storage import ECSEphemeralStorage
from .ecs_inference_accelerator import ECSInferenceAccelerator
from .ecs_tag import ECSTag
from .ecs_task_ephemeral_storage import ECSTaskEphemeralStorage
from .ecs_task_override import ECSTaskOverride
from .ecs_trusted_execution_summary import ECSTrustedExecutionSummary


class ECSTask(BaseModel):
    attachments: list[ECSAttachment] | None = None
    attributes: list[ECSAttribute] | None = None
    availabilityZone: StrictStr | None = None
    capacityProviderName: StrictStr | None = None
    clusterArn: StrictStr | None = None
    connectivity: StrictStr | None = None
    connectivityAt: datetime.datetime | StrictStr | None = None
    containerInstanceArn: StrictStr | None = None
    containers: list[ECSContainer] | None = None
    cpu: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    desiredStatus: StrictStr | None = None
    enableExecuteCommand: StrictBool | None = None
    executionStoppedAt: datetime.datetime | StrictStr | None = None
    group: StrictStr | None = None
    healthStatus: StrictStr | None = None
    inferenceAccelerators: list[ECSInferenceAccelerator] | None = None
    lastStatus: StrictStr | None = None
    launchType: StrictStr | None = None
    memory: StrictStr | None = None
    overrides: ECSTaskOverride | None = None
    platformVersion: StrictStr | None = None
    platformFamily: StrictStr | None = None
    pullStartedAt: datetime.datetime | StrictStr | None = None
    pullStoppedAt: datetime.datetime | StrictStr | None = None
    startedAt: datetime.datetime | StrictStr | None = None
    startedBy: StrictStr | None = None
    stopCode: StrictStr | None = None
    stoppedAt: datetime.datetime | StrictStr | None = None
    stoppedReason: StrictStr | None = None
    stoppingAt: datetime.datetime | StrictStr | None = None
    tags: list[ECSTag] | None = None
    taskArn: StrictStr | None = None
    taskDefinitionArn: StrictStr | None = None
    version: StrictInt | None = None
    ephemeralStorage: ECSEphemeralStorage | None = None
    fargateEphemeralStorage: ECSTaskEphemeralStorage | None = None
    trustedExecutionSummary: ECSTrustedExecutionSummary | None = None
