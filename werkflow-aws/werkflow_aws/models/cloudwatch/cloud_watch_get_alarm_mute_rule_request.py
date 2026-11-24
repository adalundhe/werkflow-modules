from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchGetAlarmMuteRuleRequest(BaseModel):
    AlarmMuteRuleName: StrictStr
