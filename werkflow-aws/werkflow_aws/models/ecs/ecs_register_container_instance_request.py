from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecs_attribute import ECSAttribute
from .ecs_platform_device import ECSPlatformDevice
from .ecs_resource import ECSResource
from .ecs_tag import ECSTag
from .ecs_version_info import ECSVersionInfo


class ECSRegisterContainerInstanceRequest(BaseModel):
    cluster: StrictStr | None = None
    instanceIdentityDocument: StrictStr | None = None
    instanceIdentityDocumentSignature: StrictStr | None = None
    totalResources: list[ECSResource] | None = None
    versionInfo: ECSVersionInfo | None = None
    containerInstanceArn: StrictStr | None = None
    attributes: list[ECSAttribute] | None = None
    platformDevices: list[ECSPlatformDevice] | None = None
    tags: list[ECSTag] | None = None
