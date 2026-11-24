from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .eks_addon_pod_identity_configuration import EKSAddonPodIdentityConfiguration


class EKSDescribeAddonConfigurationResponse(BaseModel):
    addonName: StrictStr | None = None
    addonVersion: StrictStr | None = None
    configurationSchema: StrictStr | None = None
    podIdentityConfiguration: list[EKSAddonPodIdentityConfiguration] | None = None
    ResponseMetadata: dict[str, Any] | None = None
