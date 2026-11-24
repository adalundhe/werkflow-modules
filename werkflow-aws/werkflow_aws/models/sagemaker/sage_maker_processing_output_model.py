from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .sage_maker_processing_feature_store_output_model import SageMakerProcessingFeatureStoreOutputModel
from .sage_maker_processing_s3_output_model import SageMakerProcessingS3OutputModel


class SageMakerProcessingOutputModel(BaseModel):
    OutputName: StrictStr | None = None
    S3Output: SageMakerProcessingS3OutputModel | None = None
    FeatureStoreOutput: SageMakerProcessingFeatureStoreOutputModel | None = None
    AppManaged: StrictBool | None = None
