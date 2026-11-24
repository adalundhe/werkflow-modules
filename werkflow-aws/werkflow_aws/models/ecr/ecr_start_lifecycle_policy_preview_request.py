from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECRStartLifecyclePolicyPreviewRequest(BaseModel):
    repositoryName: StrictStr
    registryId: StrictStr | None = None
    lifecyclePolicyText: StrictStr | None = None
