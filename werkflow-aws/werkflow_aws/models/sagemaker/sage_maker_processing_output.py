from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .sage_maker_processing_feature_store_output import SageMakerProcessingFeatureStoreOutput
from .sage_maker_processing_s3_output import SageMakerProcessingS3Output


class SageMakerProcessingOutput(BaseModel):
    OutputName: StrictStr | None = None
    S3Output: SageMakerProcessingS3Output | None = None
    FeatureStoreOutput: SageMakerProcessingFeatureStoreOutput | None = None
    AppManaged: StrictBool | None = None
