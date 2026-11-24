from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerModelPackageStatusItem(BaseModel):
    Name: StrictStr | None = None
    Status: StrictStr | None = None
    FailureReason: StrictStr | None = None
