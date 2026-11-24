from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_hub_access_config_model import SageMakerHubAccessConfigModel
from .sage_maker_model_access_config_model import SageMakerModelAccessConfigModel


class SageMakerS3DataSourceModel(BaseModel):
    S3DataType: StrictStr | None = None
    S3Uri: StrictStr | None = None
    S3DataDistributionType: StrictStr | None = None
    AttributeNames: list[StrictStr] | None = None
    InstanceGroupNames: list[StrictStr] | None = None
    ModelAccessConfig: SageMakerModelAccessConfigModel | None = None
    HubAccessConfig: SageMakerHubAccessConfigModel | None = None
