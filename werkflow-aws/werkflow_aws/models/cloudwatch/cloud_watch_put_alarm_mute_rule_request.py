from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .cloud_watch_mute_targets import CloudWatchMuteTargets
from .cloud_watch_rule import CloudWatchRule
from .cloud_watch_tag_model import CloudWatchTagModel


class CloudWatchPutAlarmMuteRuleRequest(BaseModel):
    Name: StrictStr
    Rule: CloudWatchRule
    Description: StrictStr | None = None
    MuteTargets: CloudWatchMuteTargets | None = None
    Tags: list[CloudWatchTagModel] | None = None
    StartDate: datetime.datetime | StrictStr | None = None
    ExpireDate: datetime.datetime | StrictStr | None = None
