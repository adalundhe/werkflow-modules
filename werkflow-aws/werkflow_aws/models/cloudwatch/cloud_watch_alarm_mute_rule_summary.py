from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class CloudWatchAlarmMuteRuleSummary(BaseModel):
    AlarmMuteRuleArn: StrictStr | None = None
    ExpireDate: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    MuteType: StrictStr | None = None
    LastUpdatedTimestamp: datetime.datetime | StrictStr | None = None
