from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECRPutLifecyclePolicyRequest(BaseModel):
    repositoryName: StrictStr
    lifecyclePolicyText: StrictStr
    registryId: StrictStr | None = None
