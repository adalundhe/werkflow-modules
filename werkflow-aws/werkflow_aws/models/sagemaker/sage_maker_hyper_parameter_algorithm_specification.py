from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_metric_definition_model import SageMakerMetricDefinitionModel


class SageMakerHyperParameterAlgorithmSpecification(BaseModel):
    TrainingImage: StrictStr | None = None
    TrainingInputMode: StrictStr | None = None
    AlgorithmName: StrictStr | None = None
    MetricDefinitions: list[SageMakerMetricDefinitionModel] | None = None
