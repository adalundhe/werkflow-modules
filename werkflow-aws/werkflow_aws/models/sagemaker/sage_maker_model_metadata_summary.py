from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerModelMetadataSummary(BaseModel):
    Domain: StrictStr | None = None
    Framework: StrictStr | None = None
    Task: StrictStr | None = None
    Model: StrictStr | None = None
    FrameworkVersion: StrictStr | None = None
