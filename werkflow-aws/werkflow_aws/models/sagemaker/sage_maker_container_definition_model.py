from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_additional_model_data_source_model import SageMakerAdditionalModelDataSourceModel
from .sage_maker_container_metrics_config_model import SageMakerContainerMetricsConfigModel
from .sage_maker_image_config_model import SageMakerImageConfigModel
from .sage_maker_model_data_source_model import SageMakerModelDataSourceModel
from .sage_maker_multi_model_config_model import SageMakerMultiModelConfigModel


class SageMakerContainerDefinitionModel(BaseModel):
    ContainerHostname: StrictStr | None = None
    Image: StrictStr | None = None
    ImageConfig: SageMakerImageConfigModel | None = None
    Mode: StrictStr | None = None
    ModelDataUrl: StrictStr | None = None
    ModelDataSource: SageMakerModelDataSourceModel | None = None
    AdditionalModelDataSources: list[SageMakerAdditionalModelDataSourceModel] | None = None
    Environment: dict[StrictStr, StrictStr] | None = None
    ModelPackageName: StrictStr | None = None
    InferenceSpecificationName: StrictStr | None = None
    MultiModelConfig: SageMakerMultiModelConfigModel | None = None
    ContainerMetricsConfig: SageMakerContainerMetricsConfigModel | None = None
