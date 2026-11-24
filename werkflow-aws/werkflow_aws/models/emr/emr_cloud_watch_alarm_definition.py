from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .emr_metric_dimension import EMRMetricDimension


class EMRCloudWatchAlarmDefinition(BaseModel):
    ComparisonOperator: StrictStr | None = None
    EvaluationPeriods: StrictInt | None = None
    MetricName: StrictStr | None = None
    Namespace: StrictStr | None = None
    Period: StrictInt | None = None
    Statistic: StrictStr | None = None
    Threshold: StrictFloat | StrictInt | None = None
    Unit: StrictStr | None = None
    Dimensions: list[EMRMetricDimension] | None = None
