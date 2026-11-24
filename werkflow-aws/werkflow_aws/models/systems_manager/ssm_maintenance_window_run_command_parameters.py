from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ssm_cloud_watch_output_config import SSMCloudWatchOutputConfig
from .ssm_notification_config import SSMNotificationConfig


class SSMMaintenanceWindowRunCommandParameters(BaseModel):
    Comment: StrictStr | None = None
    CloudWatchOutputConfig: SSMCloudWatchOutputConfig | None = None
    DocumentHash: StrictStr | None = None
    DocumentHashType: StrictStr | None = None
    DocumentVersion: StrictStr | None = None
    NotificationConfig: SSMNotificationConfig | None = None
    OutputS3BucketName: StrictStr | None = None
    OutputS3KeyPrefix: StrictStr | None = None
    Parameters: dict[StrictStr, list[StrictStr]] | None = None
    ServiceRoleArn: StrictStr | None = None
    TimeoutSeconds: StrictInt | None = None
