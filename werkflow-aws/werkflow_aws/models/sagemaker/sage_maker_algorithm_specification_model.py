from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .sage_maker_metric_definition_model import SageMakerMetricDefinitionModel
from .sage_maker_training_image_config_model import SageMakerTrainingImageConfigModel


class SageMakerAlgorithmSpecificationModel(BaseModel):
    TrainingImage: StrictStr | None = None
    AlgorithmName: StrictStr | None = None
    TrainingInputMode: StrictStr | None = None
    MetricDefinitions: list[SageMakerMetricDefinitionModel] | None = None
    EnableSageMakerMetricsTimeSeries: StrictBool | None = None
    ContainerEntrypoint: list[StrictStr] | None = None
    ContainerArguments: list[StrictStr] | None = None
    TrainingImageConfig: SageMakerTrainingImageConfigModel | None = None
