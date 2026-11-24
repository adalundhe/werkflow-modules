from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerEMRServerlessStepMetadata(BaseModel):
    ApplicationId: StrictStr | None = None
    JobRunId: StrictStr | None = None
    JobRunName: StrictStr | None = None
    LogFilePath: StrictStr | None = None
