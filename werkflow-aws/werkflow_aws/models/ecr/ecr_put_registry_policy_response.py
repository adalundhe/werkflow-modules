from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ECRPutRegistryPolicyResponse(BaseModel):
    registryId: StrictStr | None = None
    policyText: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
