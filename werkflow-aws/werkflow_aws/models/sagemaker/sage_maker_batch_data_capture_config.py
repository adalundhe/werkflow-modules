from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SageMakerBatchDataCaptureConfig(BaseModel):
    DestinationS3Uri: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    GenerateInferenceId: StrictBool | None = None
