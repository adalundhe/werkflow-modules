from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kinesis_analytics_run_configuration import KinesisAnalyticsRunConfiguration


class KinesisAnalyticsStartApplicationRequest(BaseModel):
    ApplicationName: StrictStr
    RunConfiguration: KinesisAnalyticsRunConfiguration | None = None
