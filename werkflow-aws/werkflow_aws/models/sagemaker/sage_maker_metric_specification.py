from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_customized_metric_specification import SageMakerCustomizedMetricSpecification
from .sage_maker_predefined_metric_specification import SageMakerPredefinedMetricSpecification


class SageMakerMetricSpecification(BaseModel):
    Predefined: SageMakerPredefinedMetricSpecification | None = None
    Customized: SageMakerCustomizedMetricSpecification | None = None
