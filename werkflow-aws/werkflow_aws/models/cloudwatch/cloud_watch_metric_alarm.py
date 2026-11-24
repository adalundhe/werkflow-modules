from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Literal
from .cloudwatch_dimension import CloudWatchDimension
from .cloudwatch_metric_data_query import CloudWatchMetricDataQuery
from .cloudwatch_statistics import CloudWatchStatistics
from .cloudwatch_unit import CloudWatchUnit


class CloudWatchMetricAlarm(BaseModel):
    AlarmName: StrictStr | None = None
    AlarmArn: StrictStr | None = None
    AlarmDescription: StrictStr | None = None
    AlarmConfigurationUpdatedTimestamp: datetime.datetime | None = None
    ActionsEnabled: StrictBool | None = None
    OKActions: list[StrictStr] | None = None
    AlarmActions: list[StrictStr] | None = None
    InsufficientDataActions: list[StrictStr] | None = None
    StateValue: Literal['OK', 'ALARM', 'INSUFFICIENT_DATA'] | None = None
    StateReason: StrictStr | None = None
    StateReasonData: StrictStr | None = None
    StateUpdatedTimestamp: datetime.datetime | None = None
    MetricName: StrictStr | None = None
    Namespace: StrictStr | None = None
    Statistic: CloudWatchStatistics | None = None
    ExtendedStatistic: StrictStr | None = None
    Dimensions: list[CloudWatchDimension] | None = None
    Period: StrictInt | None = None
    Unit: CloudWatchUnit | None = None
    EvaluationPeriods: StrictInt | None = None
    DatapointsToAlarm: StrictInt | None = None
    Threshold: StrictFloat | None = None
    ComparisonOperator: StrictStr | None = None
    TreatMissingData: StrictStr | None = None
    EvaluateLowSampleCountPercentile: StrictStr | None = None
    Metrics: list[CloudWatchMetricDataQuery] | None = None
    ThresholdMetricId: StrictStr | None = None
