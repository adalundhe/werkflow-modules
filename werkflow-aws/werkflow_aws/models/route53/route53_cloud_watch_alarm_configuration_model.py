from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .route53_dimension_model import Route53DimensionModel


class Route53CloudWatchAlarmConfigurationModel(BaseModel):
    EvaluationPeriods: StrictInt | None = None
    Threshold: StrictFloat | StrictInt | None = None
    ComparisonOperator: StrictStr | None = None
    Period: StrictInt | None = None
    MetricName: StrictStr | None = None
    Namespace: StrictStr | None = None
    Statistic: StrictStr | None = None
    Dimensions: list[Route53DimensionModel] | None = None
