from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_hub_access_config import SageMakerHubAccessConfig
from .sage_maker_model_access_config import SageMakerModelAccessConfig
from .sage_maker_s3_data_distribution import SageMakerS3DataDistribution
from .sage_maker_s3_data_type import SageMakerS3DataType


class SageMakerS3DataSource(BaseModel):
    S3DataType: SageMakerS3DataType | None = None
    S3Uri: StrictStr | None = None
    S3DataDistributionType: SageMakerS3DataDistribution | None = None
    AttributeNames: list[StrictStr] | None = None
    InstanceGroupNames: list[StrictStr] | None = None
    ModelAccessConfig: SageMakerModelAccessConfig | None = None
    HubAccessConfig: SageMakerHubAccessConfig | None = None
