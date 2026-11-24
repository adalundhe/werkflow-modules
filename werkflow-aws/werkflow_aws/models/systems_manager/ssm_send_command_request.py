from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .ssm_alarm_configuration import SSMAlarmConfiguration
from .ssm_cloud_watch_output_config import SSMCloudWatchOutputConfig
from .ssm_notification_config import SSMNotificationConfig
from .ssm_target import SSMTarget


class SSMSendCommandRequest(BaseModel):
    DocumentName: StrictStr
    InstanceIds: list[StrictStr] | None = None
    Targets: list[SSMTarget] | None = None
    DocumentVersion: StrictStr | None = None
    DocumentHash: StrictStr | None = None
    DocumentHashType: Literal['Sha256', 'Sha1'] | None = None
    TimeoutSeconds: StrictInt | None = None
    Comment: StrictStr | None = None
    Parameters: dict[StrictStr, list[StrictStr]] | None = None
    OutputS3Region: StrictStr | None = None
    OutputS3BucketName: StrictStr | None = None
    OutputS3KeyPrefix: StrictStr | None = None
    MaxConcurrency: StrictStr | None = None
    MaxErrors: StrictStr | None = None
    ServiceRoleArn: StrictStr | None = None
    NotificationConfig: SSMNotificationConfig | None = None
    CloudWatchOutputConfig: SSMCloudWatchOutputConfig | None = None
    AlarmConfiguration: SSMAlarmConfiguration | None = None
