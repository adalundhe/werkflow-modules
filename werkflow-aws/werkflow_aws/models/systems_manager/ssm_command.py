from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .ssm_alarm_configuration import SSMAlarmConfiguration
from .ssm_alarm_state_information import SSMAlarmStateInformation
from .ssm_cloud_watch_output_config import SSMCloudWatchOutputConfig
from .ssm_notification_config import SSMNotificationConfig
from .ssm_target import SSMTarget


class SSMCommand(BaseModel):
    CommandId: StrictStr | None = None
    DocumentName: StrictStr | None = None
    DocumentVersion: StrictStr | None = None
    Comment: StrictStr | None = None
    ExpiresAfter: datetime.datetime | StrictStr | None = None
    Parameters: dict[StrictStr, list[StrictStr]] | None = None
    InstanceIds: list[StrictStr] | None = None
    Targets: list[SSMTarget] | None = None
    RequestedDateTime: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    StatusDetails: StrictStr | None = None
    OutputS3Region: StrictStr | None = None
    OutputS3BucketName: StrictStr | None = None
    OutputS3KeyPrefix: StrictStr | None = None
    MaxConcurrency: StrictStr | None = None
    MaxErrors: StrictStr | None = None
    TargetCount: StrictInt | None = None
    CompletedCount: StrictInt | None = None
    ErrorCount: StrictInt | None = None
    DeliveryTimedOutCount: StrictInt | None = None
    ServiceRole: StrictStr | None = None
    NotificationConfig: SSMNotificationConfig | None = None
    CloudWatchOutputConfig: SSMCloudWatchOutputConfig | None = None
    TimeoutSeconds: StrictInt | None = None
    AlarmConfiguration: SSMAlarmConfiguration | None = None
    TriggeredAlarms: list[SSMAlarmStateInformation] | None = None
