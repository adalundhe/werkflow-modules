from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from .cloud_watch_action_configuration import CloudWatchActionConfiguration
from .cloud_watch_dimension_model import CloudWatchDimensionModel
from .cloud_watch_evaluation_criteria import CloudWatchEvaluationCriteria
from .cloud_watch_evaluation_window import CloudWatchEvaluationWindow
from .cloud_watch_metric_data_query_model import CloudWatchMetricDataQueryModel
from .cloud_watch_warm_up_configuration import CloudWatchWarmUpConfiguration


class CloudWatchMetricAlarmModel(BaseModel):
    AlarmName: StrictStr | None = None
    AlarmArn: StrictStr | None = None
    AlarmDescription: StrictStr | None = None
    AlarmConfigurationUpdatedTimestamp: datetime.datetime | StrictStr | None = None
    ActionsEnabled: StrictBool | None = None
    OKActions: list[StrictStr] | None = None
    AlarmActions: list[StrictStr] | None = None
    InsufficientDataActions: list[StrictStr] | None = None
    StateValue: StrictStr | None = None
    StateReason: StrictStr | None = None
    StateReasonData: StrictStr | None = None
    StateUpdatedTimestamp: datetime.datetime | StrictStr | None = None
    MetricName: StrictStr | None = None
    Namespace: StrictStr | None = None
    Statistic: StrictStr | None = None
    ExtendedStatistic: StrictStr | None = None
    Dimensions: list[CloudWatchDimensionModel] | None = None
    Period: StrictInt | None = None
    Unit: StrictStr | None = None
    EvaluationPeriods: StrictInt | None = None
    DatapointsToAlarm: StrictInt | None = None
    Threshold: StrictFloat | StrictInt | None = None
    ComparisonOperator: StrictStr | None = None
    TreatMissingData: StrictStr | None = None
    EvaluateLowSampleCountPercentile: StrictStr | None = None
    Metrics: list[CloudWatchMetricDataQueryModel] | None = None
    ThresholdMetricId: StrictStr | None = None
    EvaluationState: StrictStr | None = None
    StateTransitionedTimestamp: datetime.datetime | StrictStr | None = None
    EvaluationWindow: CloudWatchEvaluationWindow | None = None
    WarmUpConfiguration: CloudWatchWarmUpConfiguration | None = None
    EvaluationCriteria: CloudWatchEvaluationCriteria | None = None
    EvaluationInterval: StrictInt | None = None
    ActionConfiguration: CloudWatchActionConfiguration | None = None
