from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class SageMakerDataCaptureConfigSummaryModel(BaseModel):
    EnableCapture: StrictBool | None = None
    CaptureStatus: StrictStr | None = None
    CurrentSamplingPercentage: StrictInt | None = None
    DestinationS3Uri: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
