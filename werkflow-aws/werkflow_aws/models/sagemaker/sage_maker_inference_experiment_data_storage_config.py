from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_capture_content_type_header_model import SageMakerCaptureContentTypeHeaderModel


class SageMakerInferenceExperimentDataStorageConfig(BaseModel):
    Destination: StrictStr | None = None
    KmsKey: StrictStr | None = None
    ContentType: SageMakerCaptureContentTypeHeaderModel | None = None
