from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerEMRStepMetadata(BaseModel):
    ClusterId: StrictStr | None = None
    StepId: StrictStr | None = None
    StepName: StrictStr | None = None
    LogFilePath: StrictStr | None = None
