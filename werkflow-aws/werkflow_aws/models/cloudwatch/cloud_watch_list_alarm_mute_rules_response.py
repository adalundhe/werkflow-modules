from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_watch_alarm_mute_rule_summary import CloudWatchAlarmMuteRuleSummary


class CloudWatchListAlarmMuteRulesResponse(BaseModel):
    AlarmMuteRuleSummaries: list[CloudWatchAlarmMuteRuleSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
