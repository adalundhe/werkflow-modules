from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_inference_hub_access_config import SageMakerInferenceHubAccessConfig
from .sage_maker_model_access_config import SageMakerModelAccessConfig
from .sage_maker_model_compression_type import SageMakerModelCompressionType
from .sage_maker_s3_model_data_type import SageMakerS3ModelDataType


class SageMakerS3ModelDataSource(BaseModel):
    S3Uri: StrictStr | None = None
    S3DataType: SageMakerS3ModelDataType | None = None
    CompressionType: SageMakerModelCompressionType | None = None
    ModelAccessConfig: SageMakerModelAccessConfig | None = None
    HubAccessConfig: SageMakerInferenceHubAccessConfig | None = None
    ManifestS3Uri: StrictStr | None = None
    ETag: StrictStr | None = None
    ManifestEtag: StrictStr | None = None
