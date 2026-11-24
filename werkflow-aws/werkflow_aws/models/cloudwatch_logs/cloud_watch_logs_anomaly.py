from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .cloud_watch_logs_log_event import CloudWatchLogsLogEvent
from .cloud_watch_logs_pattern_token import CloudWatchLogsPatternToken


class CloudWatchLogsAnomaly(BaseModel):
    anomalyId: StrictStr | None = None
    patternId: StrictStr | None = None
    anomalyDetectorArn: StrictStr | None = None
    patternString: StrictStr | None = None
    patternRegex: StrictStr | None = None
    priority: StrictStr | None = None
    firstSeen: StrictInt | None = None
    lastSeen: StrictInt | None = None
    description: StrictStr | None = None
    active: StrictBool | None = None
    state: StrictStr | None = None
    histogram: dict[StrictStr, StrictInt] | None = None
    logSamples: list[CloudWatchLogsLogEvent] | None = None
    patternTokens: list[CloudWatchLogsPatternToken] | None = None
    logGroupArnList: list[StrictStr] | None = None
    suppressed: StrictBool | None = None
    suppressedDate: StrictInt | None = None
    suppressedUntil: StrictInt | None = None
    isPatternLevelSuppression: StrictBool | None = None
