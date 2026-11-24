from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_additional_model_data_source import SageMakerAdditionalModelDataSource
from .sage_maker_container_metrics_config import SageMakerContainerMetricsConfig
from .sage_maker_container_mode import SageMakerContainerMode
from .sage_maker_image_config import SageMakerImageConfig
from .sage_maker_model_data_source import SageMakerModelDataSource
from .sage_maker_multi_model_config import SageMakerMultiModelConfig


class SageMakerContainerDefinition(BaseModel):
    ContainerHostname: StrictStr | None = None
    Image: StrictStr | None = None
    ImageConfig: SageMakerImageConfig | None = None
    Mode: SageMakerContainerMode | None = None
    ModelDataUrl: StrictStr | None = None
    ModelDataSource: SageMakerModelDataSource | None = None
    AdditionalModelDataSources: list[SageMakerAdditionalModelDataSource] | None = None
    Environment: dict[StrictStr, StrictStr] | None = None
    ModelPackageName: StrictStr | None = None
    InferenceSpecificationName: StrictStr | None = None
    MultiModelConfig: SageMakerMultiModelConfig | None = None
    ContainerMetricsConfig: SageMakerContainerMetricsConfig | None = None
