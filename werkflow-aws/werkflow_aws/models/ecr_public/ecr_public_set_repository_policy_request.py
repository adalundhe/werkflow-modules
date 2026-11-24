from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ECRPublicSetRepositoryPolicyRequest(BaseModel):
    repositoryName: StrictStr
    policyText: StrictStr
    registryId: StrictStr | None = None
    force: StrictBool | None = None
