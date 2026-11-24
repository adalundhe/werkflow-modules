from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerClusterLifeCycleConfig(BaseModel):
    SourceS3Uri: StrictStr | None = None
    OnCreate: StrictStr | None = None
    OnInitComplete: StrictStr | None = None
