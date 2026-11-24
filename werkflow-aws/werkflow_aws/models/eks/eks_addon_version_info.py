from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .eks_compatibility import EKSCompatibility


class EKSAddonVersionInfo(BaseModel):
    addonVersion: StrictStr | None = None
    architecture: list[StrictStr] | None = None
    computeTypes: list[StrictStr] | None = None
    compatibilities: list[EKSCompatibility] | None = None
    requiresConfiguration: StrictBool | None = None
    requiresIamPermissions: StrictBool | None = None
