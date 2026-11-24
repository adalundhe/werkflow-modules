from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .sage_maker_additional_model_data_source_model import SageMakerAdditionalModelDataSourceModel
from .sage_maker_additional_s3_data_source import SageMakerAdditionalS3DataSource
from .sage_maker_base_model import SageMakerBaseModel
from .sage_maker_model_data_source_model import SageMakerModelDataSourceModel
from .sage_maker_model_input import SageMakerModelInput


class SageMakerModelPackageContainerDefinition(BaseModel):
    ContainerHostname: StrictStr | None = None
    Image: StrictStr | None = None
    ImageDigest: StrictStr | None = None
    ModelDataUrl: StrictStr | None = None
    ModelDataSource: SageMakerModelDataSourceModel | None = None
    ProductId: StrictStr | None = None
    Environment: dict[StrictStr, StrictStr] | None = None
    ModelInput: SageMakerModelInput | None = None
    Framework: StrictStr | None = None
    FrameworkVersion: StrictStr | None = None
    NearestModelName: StrictStr | None = None
    AdditionalModelDataSources: list[SageMakerAdditionalModelDataSourceModel] | None = None
    AdditionalS3DataSource: SageMakerAdditionalS3DataSource | None = None
    ModelDataETag: StrictStr | None = None
    IsCheckpoint: StrictBool | None = None
    BaseModel: SageMakerBaseModel | None = None
