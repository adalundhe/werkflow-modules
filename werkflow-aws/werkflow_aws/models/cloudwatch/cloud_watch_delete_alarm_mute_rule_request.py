from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchDeleteAlarmMuteRuleRequest(BaseModel):
    AlarmMuteRuleName: StrictStr
