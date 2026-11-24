from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ssm_cloud_watch_output_config import SSMCloudWatchOutputConfig
from .ssm_command_plugin import SSMCommandPlugin
from .ssm_notification_config import SSMNotificationConfig


class SSMCommandInvocation(BaseModel):
    CommandId: StrictStr | None = None
    InstanceId: StrictStr | None = None
    InstanceName: StrictStr | None = None
    Comment: StrictStr | None = None
    DocumentName: StrictStr | None = None
    DocumentVersion: StrictStr | None = None
    RequestedDateTime: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    StatusDetails: StrictStr | None = None
    TraceOutput: StrictStr | None = None
    StandardOutputUrl: StrictStr | None = None
    StandardErrorUrl: StrictStr | None = None
    CommandPlugins: list[SSMCommandPlugin] | None = None
    ServiceRole: StrictStr | None = None
    NotificationConfig: SSMNotificationConfig | None = None
    CloudWatchOutputConfig: SSMCloudWatchOutputConfig | None = None
