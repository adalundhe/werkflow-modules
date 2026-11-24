from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from .security_hub_aws_cloud_watch_alarm_dimensions_details import SecurityHubAwsCloudWatchAlarmDimensionsDetails


class SecurityHubAwsCloudWatchAlarmDetails(BaseModel):
    ActionsEnabled: StrictBool | None = None
    AlarmActions: list[StrictStr] | None = None
    AlarmArn: StrictStr | None = None
    AlarmConfigurationUpdatedTimestamp: StrictStr | None = None
    AlarmDescription: StrictStr | None = None
    AlarmName: StrictStr | None = None
    ComparisonOperator: StrictStr | None = None
    DatapointsToAlarm: StrictInt | None = None
    Dimensions: list[SecurityHubAwsCloudWatchAlarmDimensionsDetails] | None = None
    EvaluateLowSampleCountPercentile: StrictStr | None = None
    EvaluationPeriods: StrictInt | None = None
    ExtendedStatistic: StrictStr | None = None
    InsufficientDataActions: list[StrictStr] | None = None
    MetricName: StrictStr | None = None
    Namespace: StrictStr | None = None
    OkActions: list[StrictStr] | None = None
    Period: StrictInt | None = None
    Statistic: StrictStr | None = None
    Threshold: StrictFloat | StrictInt | None = None
    ThresholdMetricId: StrictStr | None = None
    TreatMissingData: StrictStr | None = None
    Unit: StrictStr | None = None
