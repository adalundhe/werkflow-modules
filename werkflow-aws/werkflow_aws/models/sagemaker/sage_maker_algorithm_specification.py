from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .sage_maker_metric_definition import SageMakerMetricDefinition
from .sage_maker_training_image_config import SageMakerTrainingImageConfig
from .sage_maker_training_input_mode import SageMakerTrainingInputMode


class SageMakerAlgorithmSpecification(BaseModel):
    TrainingImage: StrictStr | None = None
    AlgorithmName: StrictStr | None = None
    TrainingInputMode: SageMakerTrainingInputMode | None = None
    MetricDefinitions: list[SageMakerMetricDefinition] | None = None
    EnableSageMakerMetricsTimeSeries: StrictBool | None = None
    ContainerEntrypoint: list[StrictStr] | None = None
    ContainerArguments: list[StrictStr] | None = None
    TrainingImageConfig: SageMakerTrainingImageConfig | None = None
