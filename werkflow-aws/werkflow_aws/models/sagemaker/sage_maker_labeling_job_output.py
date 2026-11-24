from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerLabelingJobOutput(BaseModel):
    OutputDatasetS3Uri: StrictStr | None = None
    FinalActiveLearningModelArn: StrictStr | None = None
