from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SageMakerPutModelPackageGroupPolicyResponse(BaseModel):
    ModelPackageGroupArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
