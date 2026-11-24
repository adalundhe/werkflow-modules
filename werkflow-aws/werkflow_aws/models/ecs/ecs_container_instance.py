from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ecs_attachment import ECSAttachment
from .ecs_attribute import ECSAttribute
from .ecs_container_instance_health_status import ECSContainerInstanceHealthStatus
from .ecs_gpu_device import ECSGpuDevice
from .ecs_resource import ECSResource
from .ecs_tag import ECSTag
from .ecs_version_info import ECSVersionInfo


class ECSContainerInstance(BaseModel):
    containerInstanceArn: StrictStr | None = None
    ec2InstanceId: StrictStr | None = None
    capacityProviderName: StrictStr | None = None
    version: StrictInt | None = None
    versionInfo: ECSVersionInfo | None = None
    remainingResources: list[ECSResource] | None = None
    registeredResources: list[ECSResource] | None = None
    status: StrictStr | None = None
    statusReason: StrictStr | None = None
    agentConnected: StrictBool | None = None
    runningTasksCount: StrictInt | None = None
    pendingTasksCount: StrictInt | None = None
    agentUpdateStatus: StrictStr | None = None
    attributes: list[ECSAttribute] | None = None
    registeredAt: datetime.datetime | StrictStr | None = None
    attachments: list[ECSAttachment] | None = None
    tags: list[ECSTag] | None = None
    healthStatus: ECSContainerInstanceHealthStatus | None = None
    gpuDevices: list[ECSGpuDevice] | None = None
