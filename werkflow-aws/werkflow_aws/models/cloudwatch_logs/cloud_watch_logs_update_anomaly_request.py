from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .cloud_watch_logs_suppression_period import CloudWatchLogsSuppressionPeriod


class CloudWatchLogsUpdateAnomalyRequest(BaseModel):
    anomalyDetectorArn: StrictStr
    anomalyId: StrictStr | None = None
    patternId: StrictStr | None = None
    suppressionType: Literal['LIMITED', 'INFINITE'] | None = None
    suppressionPeriod: CloudWatchLogsSuppressionPeriod | None = None
    baseline: StrictBool | None = None
