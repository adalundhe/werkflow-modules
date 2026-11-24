from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .kinesis_analytics_output import KinesisAnalyticsOutput


class KinesisAnalyticsAddApplicationOutputRequest(BaseModel):
    ApplicationName: StrictStr
    CurrentApplicationVersionId: StrictInt
    Output: KinesisAnalyticsOutput
