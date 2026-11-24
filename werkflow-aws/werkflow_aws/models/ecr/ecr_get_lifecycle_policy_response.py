from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class ECRGetLifecyclePolicyResponse(BaseModel):
    registryId: StrictStr | None = None
    repositoryName: StrictStr | None = None
    lifecyclePolicyText: StrictStr | None = None
    lastEvaluatedAt: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
