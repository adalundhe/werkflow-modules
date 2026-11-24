from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .cloud_watch_logs_log_group_impact import CloudWatchLogsLogGroupImpact


class CloudWatchLogsDryRunResult(BaseModel):
    totalMatchedLogGroups: StrictInt | None = None
    increasedRetentionLogGroupCount: StrictInt | None = None
    decreasedRetentionLogGroupCount: StrictInt | None = None
    unchangedRetentionLogGroupCount: StrictInt | None = None
    failedAnalysisCount: StrictInt | None = None
    topLogGroupsImpacted: list[CloudWatchLogsLogGroupImpact] | None = None
