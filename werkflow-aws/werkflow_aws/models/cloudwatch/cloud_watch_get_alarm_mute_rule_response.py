from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_watch_mute_targets import CloudWatchMuteTargets
from .cloud_watch_rule import CloudWatchRule


class CloudWatchGetAlarmMuteRuleResponse(BaseModel):
    Name: StrictStr | None = None
    AlarmMuteRuleArn: StrictStr | None = None
    Description: StrictStr | None = None
    Rule: CloudWatchRule | None = None
    MuteTargets: CloudWatchMuteTargets | None = None
    StartDate: datetime.datetime | StrictStr | None = None
    ExpireDate: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    LastUpdatedTimestamp: datetime.datetime | StrictStr | None = None
    MuteType: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
