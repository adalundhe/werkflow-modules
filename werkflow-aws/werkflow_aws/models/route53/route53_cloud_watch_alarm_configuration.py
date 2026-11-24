from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .route53_comparison_operator import Route53ComparisonOperator
from .route53_dimension import Route53Dimension
from .route53_statistic import Route53Statistic


class Route53CloudWatchAlarmConfiguration(BaseModel):
    EvaluationPeriods: StrictInt | None = None
    Threshold: StrictFloat | None = None
    ComparisonOperator: Route53ComparisonOperator | None = None
    Period: StrictInt | None = None
    MetricName: StrictStr | None = None
    Namespace: StrictStr | None = None
    Statistic: Route53Statistic | None = None
    Dimensions: list[Route53Dimension] | None = None
