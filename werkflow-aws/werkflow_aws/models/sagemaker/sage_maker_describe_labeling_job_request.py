from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeLabelingJobRequest(BaseModel):
    LabelingJobName: StrictStr
