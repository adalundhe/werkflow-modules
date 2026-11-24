from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .sage_maker_capture_content_type_header import SageMakerCaptureContentTypeHeader
from .sage_maker_capture_option import SageMakerCaptureOption


class SageMakerDataCaptureConfig(BaseModel):
    EnableCapture: StrictBool | None = None
    InitialSamplingPercentage: StrictInt | None = None
    DestinationS3Uri: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    CaptureOptions: list[SageMakerCaptureOption] | None = None
    CaptureContentTypeHeader: SageMakerCaptureContentTypeHeader | None = None
