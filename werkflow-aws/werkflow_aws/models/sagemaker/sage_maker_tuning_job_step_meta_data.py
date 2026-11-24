from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerTuningJobStepMetaData(BaseModel):
    Arn: StrictStr | None = None
