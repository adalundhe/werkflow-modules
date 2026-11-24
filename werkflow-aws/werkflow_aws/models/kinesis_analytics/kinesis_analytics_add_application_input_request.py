from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .kinesis_analytics_input import KinesisAnalyticsInput


class KinesisAnalyticsAddApplicationInputRequest(BaseModel):
    ApplicationName: StrictStr
    CurrentApplicationVersionId: StrictInt
    Input: KinesisAnalyticsInput
