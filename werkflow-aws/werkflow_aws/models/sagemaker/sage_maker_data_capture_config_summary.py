from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .sage_maker_capture_status import SageMakerCaptureStatus


class SageMakerDataCaptureConfigSummary(BaseModel):
    EnableCapture: StrictBool | None = None
    CaptureStatus: SageMakerCaptureStatus | None = None
    CurrentSamplingPercentage: StrictInt | None = None
    DestinationS3Uri: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
