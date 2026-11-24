from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_inference_hub_access_config_model import SageMakerInferenceHubAccessConfigModel
from .sage_maker_model_access_config_model import SageMakerModelAccessConfigModel


class SageMakerS3ModelDataSourceModel(BaseModel):
    S3Uri: StrictStr | None = None
    S3DataType: StrictStr | None = None
    CompressionType: StrictStr | None = None
    ModelAccessConfig: SageMakerModelAccessConfigModel | None = None
    HubAccessConfig: SageMakerInferenceHubAccessConfigModel | None = None
    ManifestS3Uri: StrictStr | None = None
    ETag: StrictStr | None = None
    ManifestEtag: StrictStr | None = None
