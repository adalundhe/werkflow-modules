from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ECRPutLifecyclePolicyResponse(BaseModel):
    registryId: StrictStr | None = None
    repositoryName: StrictStr | None = None
    lifecyclePolicyText: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
