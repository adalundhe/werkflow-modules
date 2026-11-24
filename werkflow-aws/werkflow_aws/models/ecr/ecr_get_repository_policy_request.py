from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECRGetRepositoryPolicyRequest(BaseModel):
    repositoryName: StrictStr
    registryId: StrictStr | None = None
