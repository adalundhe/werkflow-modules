from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .cloud_watch_action_configuration import CloudWatchActionConfiguration
from .cloud_watch_tag_model import CloudWatchTagModel


class CloudWatchPutCompositeAlarmRequest(BaseModel):
    AlarmName: StrictStr
    AlarmRule: StrictStr
    ActionsEnabled: StrictBool | None = None
    AlarmActions: list[StrictStr] | None = None
    AlarmDescription: StrictStr | None = None
    InsufficientDataActions: list[StrictStr] | None = None
    OKActions: list[StrictStr] | None = None
    Tags: list[CloudWatchTagModel] | None = None
    ActionsSuppressor: StrictStr | None = None
    ActionsSuppressorWaitPeriod: StrictInt | None = None
    ActionsSuppressorExtensionPeriod: StrictInt | None = None
    ActionConfiguration: CloudWatchActionConfiguration | None = None
