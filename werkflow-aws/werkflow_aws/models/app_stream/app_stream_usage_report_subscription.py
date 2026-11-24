from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .app_stream_last_report_generation_execution_error import AppStreamLastReportGenerationExecutionError


class AppStreamUsageReportSubscription(BaseModel):
    S3BucketName: StrictStr | None = None
    Schedule: StrictStr | None = None
    LastGeneratedReportDate: datetime.datetime | StrictStr | None = None
    SubscriptionErrors: list[AppStreamLastReportGenerationExecutionError] | None = None
