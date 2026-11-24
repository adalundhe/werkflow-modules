from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECRGetLifecyclePolicyRequest(BaseModel):
    repositoryName: StrictStr
    registryId: StrictStr | None = None
