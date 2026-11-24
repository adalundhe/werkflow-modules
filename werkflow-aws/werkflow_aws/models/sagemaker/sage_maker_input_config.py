from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerInputConfig(BaseModel):
    S3Uri: StrictStr | None = None
    DataInputConfig: StrictStr | None = None
    Framework: StrictStr | None = None
    FrameworkVersion: StrictStr | None = None
