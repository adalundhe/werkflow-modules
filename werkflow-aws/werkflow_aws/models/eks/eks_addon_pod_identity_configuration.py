from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSAddonPodIdentityConfiguration(BaseModel):
    serviceAccount: StrictStr | None = None
    recommendedManagedPolicies: list[StrictStr] | None = None
