from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from .cloud_watch_action_configuration import CloudWatchActionConfiguration
from .cloud_watch_scheduled_query_configuration import CloudWatchScheduledQueryConfiguration
from .cloud_watch_tag_model import CloudWatchTagModel
from .cloud_watch_warm_up_configuration import CloudWatchWarmUpConfiguration


class CloudWatchPutLogAlarmRequest(BaseModel):
    AlarmName: StrictStr
    ScheduledQueryConfiguration: CloudWatchScheduledQueryConfiguration
    QueryResultsToEvaluate: StrictInt
    QueryResultsToAlarm: StrictInt
    Threshold: StrictFloat | StrictInt
    ComparisonOperator: Literal['GreaterThanOrEqualToThreshold', 'GreaterThanThreshold', 'LessThanThreshold', 'LessThanOrEqualToThreshold', 'LessThanLowerOrGreaterThanUpperThreshold', 'LessThanLowerThreshold', 'GreaterThanUpperThreshold']
    AlarmDescription: StrictStr | None = None
    ActionLogLineCount: StrictInt | None = None
    ActionLogLineRoleArn: StrictStr | None = None
    ActionsEnabled: StrictBool | None = None
    OKActions: list[StrictStr] | None = None
    AlarmActions: list[StrictStr] | None = None
    InsufficientDataActions: list[StrictStr] | None = None
    TreatMissingData: StrictStr | None = None
    Tags: list[CloudWatchTagModel] | None = None
    WarmUpConfiguration: CloudWatchWarmUpConfiguration | None = None
    ActionConfiguration: CloudWatchActionConfiguration | None = None
