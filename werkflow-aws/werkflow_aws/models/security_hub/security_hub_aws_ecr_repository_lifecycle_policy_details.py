from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEcrRepositoryLifecyclePolicyDetails(BaseModel):
    LifecyclePolicyText: StrictStr | None = None
    RegistryId: StrictStr | None = None
